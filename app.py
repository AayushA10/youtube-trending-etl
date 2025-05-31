import streamlit as st
from db import load_data
import plotly.express as px

st.set_page_config(page_title="YouTube Trending Dashboard", layout="wide")

st.title("📈 YouTube Trending Videos Dashboard")

df = load_data()

# Show Data Table
st.subheader("All Trending Videos")
st.dataframe(df)

# Top 10 Videos by Views
st.subheader("Top 10 Videos by Views")
top_videos = df.sort_values(by='view_count', ascending=False).head(10)
fig_views = px.bar(top_videos, x='title', y='view_count', title='Top 10 Videos by Views', labels={'title':'Video Title', 'view_count':'View Count'})
st.plotly_chart(fig_views)

# Top 10 Videos by Likes
st.subheader("Top 10 Videos by Likes")
top_likes = df.sort_values(by='like_count', ascending=False).head(10)
fig_likes = px.bar(top_likes, x='title', y='like_count', title='Top 10 Videos by Likes', labels={'title':'Video Title', 'like_count':'Like Count'})
st.plotly_chart(fig_likes)

# Distribution by Category ID
st.subheader("Distribution by Category ID")
category_dist = df['category_id'].value_counts().reset_index()
category_dist.columns = ['category_id', 'count']
fig_category = px.pie(category_dist, names='category_id', values='count', title='Category-wise Distribution')
st.plotly_chart(fig_category)

# Channel-wise Filter
st.subheader("Filter by Channel")
channels = st.selectbox("Select a Channel", options=df['channel_title'].unique())
filtered_df = df[df['channel_title'] == channels]
st.dataframe(filtered_df)
