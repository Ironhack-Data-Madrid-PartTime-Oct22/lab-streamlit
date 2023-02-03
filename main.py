import streamlit as st
import src.soporte_hotels as sp
import pandas as pd

st.image("images/portada_color.jpeg", width=700)

st.title(':orange[TRAVEL + LEISURE HOTELS]')

st.write("<style>body { font-family: 'Comic Sans MS'; }</style>", unsafe_allow_html=True)
st.write("Travel and Leisure is a magazine and website that focuses on travel, food and \n lifestyle topics. It provides readers with information and inspiration for \n planning trips, discovering new destinations, and experiencing the best in dining, \n shopping and culture around the world. It also covers topics such as home design, \n wellness and travel news.")

st.write("Where do you want to travel to? Select the following features and I will show you the hotels and ratings from the ranking of the 100 best hotels of 2022 and 2021 proposed by Travel and Leisure magazine.")

df = sp.open_csv_pandas("data/df_all_hotel_data.csv")

regions_options = df["Region"].unique()
region_selected = st.selectbox("Select a :orange[**region**:]", regions_options)

filtered_df = df[df["Region"] == region_selected]
country_options = filtered_df["Country"].unique()
selected_country = st.selectbox("Select a :orange[**country**]", country_options)

filtered_df = filtered_df[filtered_df["Country"] == selected_country]
city_options = filtered_df["Location"].unique()
selected_city = st.selectbox("Select a :orange[**city**:]", city_options)

st.write("The best hotel(s) in the city selected are presented below with the corresponding \n review of :green[Trip Advisor] and :blue[Google Reviews]:")

if selected_city:
    filtered_df = sp.filter_by_city(df, selected_city)
    st.dataframe(filtered_df)
else:
    st.write("There aren't hotels the selected location")


result_df = sp.compare_result_df(df, filtered_df)
#st.dataframe(result_df)
web_options = pd.DataFrame({'Web': ["TripAdvisor", "Google Reviews"]})
selected_web = st.selectbox("Select a :orange[**web review**:]", web_options)


if selected_web == "TripAdvisor":
    sp.bar_chart(result_df, "Comparison with Tripavisor", 'Hotel', 'Trip_Rate', "green")
elif selected_web == "Google Reviews":
    sp.bar_chart(result_df, "Comparison with Google reviews",'Hotel', 'Google_Rate', "blue")
else:
    st.write("Cant offer you a comparison")



