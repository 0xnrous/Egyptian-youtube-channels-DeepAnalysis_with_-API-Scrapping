import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as  sns

# Set page configuration
st.set_page_config(
    page_title='📺 YouTube Channel Data Analytics',
    page_icon='🎥',
    layout='wide'
)

# Sidebar
st.sidebar.success("Made with ❤️ / Created by 0XNROUS")

# Header section
header = st.container()
with header:
    st.title("👨🏾‍🏫 Droos Online Channel Analytics")
    img = st.image("last.jpg", caption=" Droos Online Channel ", use_column_width=True)

# Read data
df_droos = pd.read_csv("Droos_Videos_years.csv")

# Dataset section
dataset_video = st.container()
with dataset_video:
    st.subheader("Dataset of Droos Online Channel Videos")
    st.write("`This Data is Genterated from YouTube API in 06/08/2023.`")
    st.write("-----------------------------------------------------------------")
    col1 , col2 = st.columns(2)
    with col1:
        show_data_button = st.button(" ⟳ Show Data")
    with col2:
        close_data_button = st.button(" ⟲ Close Data")

    if show_data_button:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("Video Title")
            st.write(df_droos['Title'])
        with col2:
            st.write("Views")
            st.write(df_droos['Views'])
        with col3:
            st.write("Month")
            st.write(df_droos['Month_name'])
        with col4:
            st.write("Year")
            st.write(df_droos['Year'])
    elif close_data_button == True:
        st.write("Data Closed.")
        

st.write("-----------------------------------------------------------------")
Qu_videos = st.container()
with Qu_videos:
    with st.expander("  🔽 🔽 🔽 🔽 Here is Some Top Questions for Effective EDA for Droos Online Channel 🔽 🔽 🔽 🔽 "):
        st.subheader("Let's Ask the Right Questions for Effective EDA")
        st.write("[Q1: What is Top videos for number of Comments, Likes and Views for Each Feature ?]")
        st.write("[Q2: What is Lowest videos for number of Comments, Likes and Views for Each Feature ?]")
        st.write("[Q3: What are Comparison between channel's growth metrics ?]")
        st.write("[Q4: Which Year of (channel_name) is Viwed , Liked and Commented Most ? ]")
        st.write("[Q5: Which Montha in 2023 of (channel_name) is have Viwes ,Likes and Comments Most ? ]")
        st.write("[Q6: What is Maximun and minumim avgerage revegue of Droos Online ?]")
        st.write("[Q7: There are any relationship between Anual Income, Years ? ]")
        st.write("[Q8: There are any relationship between Anual Income, Month Name ? ]")
        st.write("[Q9: Correlation Coefficient Matrix of Droos Online `Views`,`Likes`, `Comments`, `maximum_income` ]")
    

viz_videos = st.container()

with viz_videos:
    st.subheader(" 📊  Visualization of Droos Online Channel Videos ")
    st.write("--------------------------------------------------")
    
    with st.expander(" >> [Q1: What is Top videos for number of Views , Likes and Comments for Each Feature ?]"):
        top10_Comments = df_droos.sort_values(by = 'Comments' ,ascending= False )[['Title','Comments' , 'thumbnails']][:10]
        top10_Viewed_videos =df_droos.sort_values(by = 'Views' ,ascending= False )[['Title','Views' , 'thumbnails']][:10]
        top10_likes = df_droos.sort_values(by = 'Likes' ,ascending= False )[['Title','Likes' , 'thumbnails']][:10]
        fig_views_top = px.histogram(x =top10_Viewed_videos['Views'], y =top10_Viewed_videos['Title'])
        fig_likes_top = px.histogram(x =top10_likes['Likes'], y =top10_likes['Title'])
        fig_Comments_top = px.histogram(x =top10_Comments['Comments'], y =top10_Comments['Title'])
        st.subheader("Top 10 Views of Droos Online Channel Videos")
        st.plotly_chart(fig_views_top)   
        st.subheader("Top 10 Likes of Droos Online Channel Videos")
        st.plotly_chart(fig_likes_top)
        st.subheader("Top 10 Comments of Droos Online Channel Videos")
        st.plotly_chart(fig_Comments_top)
        st.subheader("Insights Of Top 10")
        Top10_insight ="> If we look at the visualization and also the values ​​that we have printed above, we can see that in likes we see that `كيف تذاكر أقل و تذاكر بذكاء ؟	` has more likes , and  in Comments we see that `Giveaway بمناسبة المليون.`,also i regonize that i need to see  correlation with each other  ,` this is because the two features are closely related ` and views the most viwed one is `1- شرح زمن المضارع البسيط Present Simple	 `."
        st.write(Top10_insight)   
        
    with st.expander("[Q2: What is Lowest videos for number of Comments, Likes and Views for Each Feature ?]"):
        lowest10_Comments = df_droos.sort_values(by = 'Comments' ,ascending= True )[['Title','Comments' , 'thumbnails']][:10]
        lowest10_Viewed_videos =df_droos.sort_values(by = 'Views' ,ascending= True )[['Title','Views' , 'thumbnails']][:10]
        lowest10_likes = df_droos.sort_values(by = 'Likes' ,ascending= True )[['Title','Likes' , 'thumbnails']][:10]
        fig_views_lowest = px.histogram(x =lowest10_Viewed_videos['Views'], y =lowest10_Viewed_videos['Title'])
        fig_likes_lowest = px.histogram(x =lowest10_likes['Likes'], y =lowest10_likes['Title'])
        fig_Comments_lowest = px.histogram(x =lowest10_Comments['Comments'], y =lowest10_Comments['Title'])
        st.subheader("Lowest 10 Views of Droos Online Channel Videos")
        st.plotly_chart(fig_views_lowest)   
        st.subheader("Lowest 10 Likes of Droos Online Channel Videos")
        st.plotly_chart(fig_likes_lowest)
        st.subheader("Lowest 10 Comments of Droos Online Channel Videos")
        st.plotly_chart(fig_Comments_lowest)
        st.subheader("Insights Of Lowest 10")
        lowest10_insight = "> If we look at the visualization and also the values ​​that we have printed above, we can see that in likes we see that `دروس أونلاين Live Stream` has less likes , and  in Comments we see that the same video has less comments ,also i recognize that i need to see  correlation with each other  ,` this is because the two features are closely related ` and views the lowest viwed one is `فيديو الجمعة دي غريب شويتين 🔴 `."
        st.write(lowest10_insight)  
    
        
    with st.expander("[Q3-1: What are Comparison between channel's growth metrics with Pairplot?]"):
        plt.figure(figsize= (2,2))
        fig_growth = sns.pairplot(df_droos[['Comments','Likes', 'Views']])
        st.pyplot(fig_growth)   
        st.subheader("Insights: ")
        st.write("> The pairplot shows that there is multiple pairwise bivariate distributions so:")
        Corr_insight_pairplot = "> We get that `Likes`, `Views`, are `highly correlated` with each other. But number of `Comments` has low correlation with the other metrics."
        st.write(Corr_insight_pairplot)     
    
    
    with st.expander("[Q3-2: What are Comparison between channel's growth metrics with Heatmap?]"):
        plt.figure(figsize= (2,2))
        fig, ax = plt.subplots() 
        sns.heatmap(df_droos[['Comments','Likes', 'Views']].corr(),ax = ax, annot = True )
        st.write(fig)
        st.subheader("Insights: ")
        st.write("> The Heatmap shows correlation between `Comments`, `Likes`, `Views`:")
        Corr_insight_heatmap = "> The heatmap proves the previous statement. So `Likes`, `Views` are equally important metrics (and maybe more important than number of `comments`) to the performance of the channel."
        st.write(Corr_insight_heatmap) 
 
        
        
    with st.expander("[Q4: Which Year of Droos Online Channel is Viwed , Liked and Commented Most ?]"):
        video_df_0_Year_viewed = df_droos.groupby(["Year"])["Views"].sum().sort_values(ascending=True).reset_index()
        video_df_0_Year_liked = df_droos.groupby(["Year"])["Likes"].sum().sort_values(ascending=True).reset_index()
        video_df_0_Year_Commented = df_droos.groupby(["Year"])["Comments"].sum().sort_values(ascending=True).reset_index()

        fig_years_views = px.bar(x = video_df_0_Year_viewed['Year'], y = video_df_0_Year_viewed['Views'])
        fig_years_likes = px.bar(x = video_df_0_Year_liked['Year'], y = video_df_0_Year_liked['Likes'])
        fig_years_comments = px.bar(x = video_df_0_Year_Commented['Year'], y = video_df_0_Year_Commented['Comments'])
        st.subheader(" Year That Channel Most Viewed ")
        st.plotly_chart(fig_years_views)
        st.write("--------------------------------------------------")
        st.subheader("Insights For Views: ")
        st.write("--------------------------------------------------")
        Years_insgights = "> If we look at the visualization and also the values ​, we can see that in `2016` has more than 93 milion views and it decrease again."
        st.write(Years_insgights)
        st.write("--------------------------------------------------")
        ################################
        st.subheader(" Year That Channel Most Commented ")
        st.plotly_chart(fig_years_comments)
        st.write("--------------------------------------------------")
        st.subheader("Insights For Comment: ")
        Years_insgights ="Now, we can see that in `2016` has 151159.0 comment and `2017` has more Commented Year than other Years ."
        st.write(Years_insgights)
        st.write("--------------------------------------------------")
        #################################
        st.subheader(" Year That Channel Most Liked ")
        st.plotly_chart(fig_years_likes)
        st.write("--------------------------------------------------")
        st.subheader("Insights for Likes: ")
        Years_Liked_insgights = " We can see that in `2016` and `2017` has more likes than other Years ."
        st.write(Years_Liked_insgights)
        st.write("--------------------------------------------------")
        
        
    with st.expander("[Q5: Which Montha in 2023 of Droos Online Channel is have Viwes ,Likes and Comments Most ? ]"):
        year23=df_droos[df_droos["Year"]==2023]
        month_2023_views=year23.groupby(["Month_name"])["Views"].sum().sort_values(ascending=False).reset_index()
        month_2023_likes=year23.groupby(["Month_name"])["Likes"].sum().sort_values(ascending=False).reset_index()
        month_2023_commented=year23.groupby(["Month_name"])["Comments"].sum().sort_values(ascending=False).reset_index()
        fig_month_view = px.histogram(x = month_2023_views['Month_name'], y = month_2023_views['Views'])
        fig_month_likes = px.histogram(x = month_2023_likes['Month_name'], y = month_2023_likes['Likes'])
        fig_month_comments = px.histogram(x = month_2023_commented['Month_name'], y = month_2023_commented['Comments'])
        #st.plotly_chart(fig_month_view)
        #st.plotly_chart(fig_month_likes)
        #st.plotly_chart(fig_month_comments)
        #########################################
        st.subheader(" Month in 2023 That Channel Most Viewed ")
        st.plotly_chart(fig_month_view)
        st.write("--------------------------------------------------")
        st.subheader("Insights Of Views in This Month of 2023: ")
        st.write("--------------------------------------------------")
        Month_Views_insgights = "> If we look at the visualization and also the values ​, we can see that in `May` has more than 2.4 milion views than other Months."
        st.write(Month_Views_insgights)
        st.write("--------------------------------------------------")
        
        ####################################################################################
        st.subheader(" Month in 2023 That Channel Most Liked ")
        st.plotly_chart(fig_month_likes)
        st.write("--------------------------------------------------")
        st.subheader("Insights Of Likes in This Month of 2023: ")
        st.write("--------------------------------------------------")
        Month_likes_insgights = "> If we look at the visualization and also the values ​, we can see that in `june` has more than 180k likes than other Months."
        st.write(Month_likes_insgights)
        st.write("--------------------------------------------------")
        
        
         ####################################################################################
         
        st.subheader(" Month in 2023 That Channel Most Commented ")
        st.plotly_chart(fig_month_comments)
        st.write("--------------------------------------------------")
        st.subheader("Insights Of Comments in This Month of 2023: ")
        st.write("--------------------------------------------------")
        Month_comments_insgights = "> If we look at the visualization and also the values ​, we can see that in `May` has more than 9000 comments than other Months."
        st.write(Month_comments_insgights)
        st.write("--------------------------------------------------")
        
    with st.expander("[Q6: What is Maximun and Minumim avgerage revegue of Droos Online ?]"):
        Total_min = df_droos['minimum_income'].sum()
        Total_max = df_droos['maximum_income'].sum()
        st.write("--------------------------------------------------")
        st.subheader("Maximun Estimated Revenue:")
        st.write(f'The Current Maximum Estimated Revenue Is: {Total_max} $')
        st.write("--------------------------------------------------")
        st.subheader("Minimun Estimated Revenue:")
        st.write(f'The Current Minimun Estimated Revenue Is: {Total_min} $')
        st.write("--------------------------------------------------")
    
    
    with st.expander("[Q7: There are any relationship between Anual Income, Years ? ]"):
        plt.figure(figsize=(20,10) , facecolor='White')
        fig = sns.barplot(x=df_droos['Year'], y=df_droos['maximum_income']).set(title="Anual Income" , facecolor='White' )
        plt.xlabel("Year")
        plt.ylabel("Income in USD")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        fig_show_1 = plt.show()
        st.subheader("Anual Income vs Years: ")
        st.pyplot(fig_show_1)
        st.write("--------------------------------------------------")
        st.subheader("Insights : ")
        st.write("--------------------------------------------------")
        Anualy_Income_insgights = "> ` We get that from__ `2012`__ to__ `2014`__ is low Anual Income less than__ `1000` $ __ and 2015 is increase highly to__ `8000` $__ , In __`2016` __is highly Annual Income to__ `10000` $__ `and `From__ `2017`__ to__ `2023`__ Annual Average is__ `3652.5`__  So it's Make Good Positive Annual Income `"
        st.write(Anualy_Income_insgights)
        st.write("--------------------------------------------------")
        
        
        
    with st.expander("[Q8: There are any relationship between Anual Income, Month Name ? ]"):
        plt.figure(figsize=(20,10) , facecolor='White')
        sns.barplot(x=df_droos['Month_name'], y=df_droos['maximum_income']).set(title="Month Income" , facecolor='White')
        plt.xlabel("Month Name")
        plt.ylabel("Income in USD")
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        fig_show_2 = plt.show()
        st.subheader("Anual Income vs Months: ")
        st.pyplot(fig_show_2)
        st.write("--------------------------------------------------")
        st.subheader("Insights : ")
        st.write("--------------------------------------------------")
        Monthly_Income_insgights = "> `We get that from__ `January`_ is Most Month that's income he take from youtube about 8000 usd  `"
        st.write(Monthly_Income_insgights)
        st.write("--------------------------------------------------")
        
        
    with st.expander("[Q9: Correlation Coefficient Matrix of Droos Online `Views`,`Likes`, `Comments`, `maximum_income` ]"):
        cols = ['Views','Likes', 'Comments', 'maximum_income']
        selected_df = df_droos[cols]
        corr_matrix = selected_df.corr()
        sns.heatmap(corr_matrix, annot=True)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        fig_show_corr = plt.show()
        st.subheader("Correlation Coefficient Matrix: ")
        st.pyplot(fig_show_corr)
        st.write("--------------------------------------------------")
        st.subheader("Insights : ")
        st.write("--------------------------------------------------")
        Corr_insgights_heatmap = "We observe a high degree of correlation among the number of likes, views, and income  and litile bit with comments.`"
        st.write(Corr_insgights_heatmap)
        st.write("--------------------------------------------------")
        
        
        





st.write("-------------------------------------------------------------------------------------------------------------")
# Define custom CSS style
custom_css = """
<style>
.highlight {
    background-color: #f7f7f7;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    font-size: 16px;
    line-height: 1.6;
    text-align: justify;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Conclusion and Insights section
conclusion = st.container()
with conclusion:
    st.subheader("Conclusion for Droos Online Channel 📕 (Final Insights):")
    
    insights_text = """
    How to Increase Video CTR, Interaction, and Subscription Ratio:
    
    - Use more action verbs.
    
    - Best CTR titles used in the channel are: “تعلم”, "وصايا", “مذاكرة”, “نصائح”, “اسهل”, “شرح”, “فقط”, “اقل”, “كيف”, 
         related to most of the top 10 videos of views, likes, and comments.
         
    - Avoid using words like “التحميل”, “ادوات”, “مشكلة”.
    
    - Create clean thumbnails with light text colors (white, yellow, sky blue) over bold colors for better click-through rates.
    
    - Avoid low CTR titles related to lives and Q&A sessions.
    
    - Refrain from using red text on dark backgrounds.
    
    - Simplify thumbnails and avoid overcrowding with multiple objects.
    
    - Avoid creating videos about tutorials for Windows programs like IDM or similar topics.
    
    - Consider using emojis to make titles more attractive.
    
    The most significant advice from this analysis is to create engaging learning videos using popular and trending study techniques, 
    as well as English tutorials, to attract a larger audience and increase views and subscribers.
    """
    
    st.markdown(f"<div class='highlight'>{insights_text}</div>", unsafe_allow_html=True)
    
st.write("-------------------------------------------------------------------------------------------------------------") 
st.info("Implementing these insights can help optimize video performance and audience engagement on Droos Online Channel.")



 
st.markdown(
    """
    <style>
    .st-e1 {
        padding: 15px;
        background-color: #f5f5f5;
    }
    .st-ca {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 10px;
    }
    .st-cb {
        margin-top: 15px;
    }
    .css-1v2f0em {
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 16px;
    }
    .css-j7ju5z {
        font-size: 22px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)
