import streamlit as st
import src.soporte_api as sa


df=sa.abrir_csv("data/df_spotify_limpio_completo.csv")

st.markdown("# 🎵 TOP SONGS & ARTIST CONCLUSIONS 🎵")
st.markdown("## 🔥 Song analysis 🔥")
sa.grafico_barras_1(df["Genre"], "Genre", "Number of Songs", "TOP 2021&2021 Songs by Genre")
st.markdown("**Pop** is **BY FAAAAAR** the 🔝 king!!! 🎵 We all know that pop can be very catchy and as elle magazine says, according to the musician, pop music is inherently popular because it creates a sense of familiarity for listeners. This is an **absolute prove** that this is an accurate afirmation!")

st.markdown("## 🤔 Does popular taste change over the year? Songs characteristics? 🤔")
st.markdown(" Human behaviours can change during the year and tastes to. Lets see if popularity characteristics values change depending on the season using the following values **Danceability Energy Speechiness Acousticness Liveness**. ")

df_group = df.groupby(['Season_Highest_Charting'])[['Danceability', 'Energy', 'Speechiness', 'Acousticness', 'Liveness']].mean().reset_index()
x= 'Season_Highest_Charting'
group=['Danceability', 'Energy', 'Speechiness', 'Acousticness', 'Liveness']

sa.barplot_grupos(df_group, x,  group, "Season", "Mean", "Songs Characteristics by year Season")
st.markdown("Most of the characteristics stay the same, but 🔥 in winter, the most popular songs have higher 🎸acoustic levels. This means more acoustic instruments and less electronic sounds. It indicates that people tend to prefer less electronic and more acoustic songs in winter, compared to other seasons. 😎")



st.markdown("## 🎤 Artists? Where do most popular artists come from?")

st.image("image/Artist_Country.png")
st.markdown("🚀🚀As you can see in the map above, most artists of my dataframe are born in USA. I dont know if US is the most music influencial country but what I can confirm is that US is the country where most influencial artist are from.🚀🚀")


df_country_codes=sa.abrir_csv("data/df_country_codes.csv")
Music_Genre=df["Genre"].unique().tolist()
Music_Genre.append("Reggaeton")
Countries=df_country_codes.index.tolist()
mytoken=sa.token()

st.markdown("# 🎵 Find your perfect Ticketmaster Event 🎵")
st.write("Use the sidebar to fill your selection")
st.sidebar.markdown("# 🎵 Find your perfect Ticketmaster Event 🎵")
st.sidebar.image("image/music_icon.png")
Genre = st.sidebar.selectbox("What is your favorite music genre?", Music_Genre)
Country = st.sidebar.selectbox("Which Country interest you for the event?", Countries)

st.markdown(f"### 🎶 You have selected: {Genre} 🎶 events in {Country} 🌍")
st.markdown("Find below ticketmaster events that match your selection")

df_event=sa.tu_request_ticketmaster(Genre, Country, df_country_codes, mytoken)
df_event

min_price, max_price = st.sidebar.slider("Select you price range:", 0, 1000, (0, 1000))
st.markdown(f"### 💰 Your selected price range: 💰 min_price: {min_price} 💰 max_price: {max_price}")
st.markdown("Find below ticketmaster events that match your price range")

df_price=sa.filter_price_range(df_event, min_price, max_price)
df_price
