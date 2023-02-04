import folium 
import pandas as pd
from IPython.display import display

def maps_world(df):
    latitude_center = df['latitude'].mean()
    longitude_center = df['longitude'].mean()
    m = folium.Map(location=[latitude_center, longitude_center], zoom_start=13)
    for i, row in df.iterrows():
        folium.Marker([row['latitude'], row['longitude']], 
                    popup='{}, {}'.format(row['language'], row['endangerment'])).add_to(m)
    m.save('map.html')
    plt.savefig("images/map_world.png")
