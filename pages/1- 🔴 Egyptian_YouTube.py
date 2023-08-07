import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import urllib.request

# Set page configuration and title
st.set_page_config(
    page_title='📺 YouTube Channel Data Analytics',
    page_icon='🎥',
    layout='wide'
)

# Set custom styling
st.markdown(
    """
    <style>
    .st-cb {
        background-color: #f5f5f5;
    }
    .css-1e26y49 {
        font-family: Monospace;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.markdown("Made with ❤️ / Created by 0XNROUS")

# Main content
page_title = st.title("🇪🇬 Egyptian YouTube Channel Analytics")
st.write("Before we start exploring the data, let's establish a clear objective to guide our analysis.")

# Display image
image = Image.open("emg.webp")
st.image(image, caption="YouTube Analytics", use_column_width=True)

# Data loading
channel_df = pd.read_csv('channel_stats.csv')

# DataFrame and Visualization sections
dataset_channels = st.container()
viz_channels = st.container()

with dataset_channels:
    st.header("All Channels Data")
    st.write("Explore the dataset to get a glimpse of the channels we've scraped from YouTube.")
    show_dataframe = st.button("Show DataFrame of All Channels")
    if show_dataframe:
        with st.expander("Channel Titles and Descriptions"):
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Title of All Channels")
                st.write(channel_df['Title'])
            with col2:
                st.subheader("Description of All Channels")
                st.write(channel_df['Description'])

with viz_channels:
    st.header("Visualizations of Channels")
    st.subheader("Let's Ask the Right Questions for Effective EDA")
    st.write("[Q1: What is the title of the video with the highest views?]")
    st.write("[Q2: What is the title of the video with the lowest views?]")
    st.write("[Q3: Which channel has the highest number of subscribers?]")
    st.write("[Q4: Which channel has the lowest number of subscribers?]")
    st.write("[Q5: Which channel has the highest number of videos?]")
    st.write("[Q6: Which channel has the lowest number of videos?]")

    with st.expander("Visualization of View_Count"):
        st.subheader("Relation between Channel Title and View Count")
        sorted_channel_df_views = channel_df.sort_values(by='View_Count', ascending=False)
        fig_views = px.histogram(sorted_channel_df_views, x="Title", y="View_Count")
        st.plotly_chart(fig_views)
        st.write("Channel with the highest views: عمر فاروق Omar Farooq")
        st.write("Channel with the lowest views: Zero Grad")

    with st.expander("Visualization of Subscribers_Count"):
        st.subheader("Relation between Channel Title and Subscribers Count")
        sorted_channel_df_subs = channel_df.sort_values(by='Subscribers_Count', ascending=False)
        fig_subs = px.histogram(sorted_channel_df_subs, x="Title", y="Subscribers_Count")
        st.plotly_chart(fig_subs)
        st.write("Channel with the highest subscribers: دروس أونلاين")
        st.write("Channel with the lowest subscribers: Zero Grad")

    with st.expander("Visualization of Video_Count"):
        st.subheader("Relation between Channel Title and Video Count")
        sorted_channel_df_videos = channel_df.sort_values(by='Video_Count', ascending=False)
        fig_videos = px.histogram(sorted_channel_df_videos, x="Title", y="Video_Count")
        st.plotly_chart(fig_videos)
        st.write("Channel with the highest video count: Amir Mounir أمير منير")
        st.write("Channel with the lowest video count: Deena Gergis")

# Insights
st.subheader("Insights")
channels_insight = 'Based on an analysis of Popular YouTube channels in Egypt, entertainment channels same as ` ويجز Wegz` ,  `دروس أونلاين` , ` CairokeeOfficial` , `Peace Cake	`  and so on  have significantly higher `likes`, `comments`, and `views ` compared to educational  or useful channels same  `وعي `  or   `Dr. Ahmed Hagag`      or    `   Zero Grad	`.'
st.write(channels_insight)    

