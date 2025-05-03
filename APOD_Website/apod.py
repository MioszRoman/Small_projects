import requests
import streamlit as st


#Get an api and url. Make a request and save it in json
api_key = "tDOjDmjVr97tedf86K0faLt4tIGWmr8btpC2ScZd"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)
data = response.json()

#Create a variables
date_of_today = data['date']
title_of_photo = data['title']
img_url = data['url']
description = data['explanation']

#Make a webpage layout using streamlit
st.title("My APOD website")
st.header(title_of_photo)
st.subheader(date_of_today)
st.image(img_url)
st.text(description)
