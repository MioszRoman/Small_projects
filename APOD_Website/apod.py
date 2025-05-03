import requests
import streamlit as st


#Get an api and url. Make a request and save it in json
api_key = "tDOjDmjVr97tedf86K0faLt4tIGWmr8btpC2ScZd"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)
data = response.json()



