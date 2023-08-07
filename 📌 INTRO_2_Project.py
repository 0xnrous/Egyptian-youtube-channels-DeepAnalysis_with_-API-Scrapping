#📺 YouTube Channel Data Analytics
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import pandas as pd 
import os 

st.set_page_config(
    page_title= '📺 YouTube Channel Data Analytics',
    page_icon= '🎥',
    layout="wide")
st.sidebar.image("logo.webp")
st.sidebar.success("Made with ❤️ / \n Created by 0XNROUS")

header = st.container()
dataset_video = st.container()
viz_videos = st.container()
insights_videos = st.container()


with header :
    st.title(" 📺 YouTube Channel Data Analytics")
    st.subheader("About My Project")
    st.write("it’s Mid Project for Data Science Diploma i build a Python Script to Scrape YouTube data using YouTube Data API. Then we extract the data and then load this data into a Python Pandas DataFrame and analyze this data. Finally, we build simple visualization from this data using the Python Seaborn and ploty library.")
    image = st.image("y.jpg")


    


