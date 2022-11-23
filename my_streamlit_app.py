import streamlit as st

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please give me your name :")
name_length = len(name)

st.write("Your name has ",name_length,"characters")

st.write("I enjoy to discover stremalit possibilities")

import pandas as pd
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
df_weather

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

import seaborn as sns
import matplotlib as plt
viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

import pandas as pd
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars

st.line_chart(df_cars['time-to-60'])

import seaborn as sns
import matplotlib as plt
viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

result1 = st.button("US")
if result1:
	st.write(df_cars["continent"]=="US.")

result2 = st.button("Europe")
if result2:
st.write(df_cars["continent"]=="Europe.")

result3 = st.button("Japan")
if result3:
st.write((df_cars["continent"]=="Japan.")
