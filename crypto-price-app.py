# First attempt at financial app. Not recommend for real #investment. Use at your risk
import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time

st.set_page_config(layout="wide")
#---------------------------------#
# Title

image = Image.open('logo.jpg')

st.image(image, width = 500)

st.title('Crypto Price App')
st.markdown("""
This app retrieves cryptocurrency prices for the top 100 cryptocurrency from the **CoinMarketCap**!
""")