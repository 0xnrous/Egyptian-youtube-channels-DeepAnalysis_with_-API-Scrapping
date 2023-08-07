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
st.sidebar.success("Made with ❤️ / \n Created by 0XNROUS")



# Header section
header = st.container()
with header:
    st.title("📚 ReadTube - جيل يقرأ Channel Analytics")
    img = st.image("g.jpg", caption="  قناة جيل يقرأ  ", use_column_width=True)
    
soon = st.container()

with soon:
    st.header ("Comming Soon ...")