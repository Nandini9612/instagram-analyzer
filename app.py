import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Instagram Analyzer (Demo)", layout="wide")
st.title("📊 Instagram Profile Analyzer (Demo Mode)")

st.write(
    "This is a **safe demo version**. It does *not* fetch real Instagram data, "
    "but simulates realistic profile stats and post performance."
)

username = st.text_input("Enter any username (demo only):", value="demo_user")

if st.button("Analyze"):
    if not username.strip():
        st.error("Please enter a username.")
    else:
        followers = random.randint(1000, 100000)
        following = random.randint(100, 5000)
        posts_count = random.randint(20, 200)

        st.success(f"Showing demo analytics for @{username}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Followers", f"{followers:,}")
        with col2:
            st.metric("Following", f"{following:,}")
        with col3:
            st.metric("Total Posts", posts_count)

        num_posts = 30
        dates = [datetime.now() - timedelta(days=i) for i in range(num_posts)]
        dates.reverse()

        likes = np.random.randint(50, 5000, size=num_posts)
        comments = np.random.randint(0, 300, size=num_posts)
        engagement = likes + comments

        df = pd.DataFrame({
            "date": dates,
            "likes": likes,
            "comments": comments,
            "engagement": engagement
        })

        st.subheader("📈 Post Performance (Demo Data)")
        st.dataframe(df)

        st.subheader("Likes Over Time")
        st.line_chart(df.set_index("date")["likes"])

        st.subheader("Engagement Over Time")
        st.line_chart(df.set_index("date")["engagement"])

        st.subheader("Summary (Demo)")
        st.write(f"- Average likes: **{int(df['likes'].mean()):,}**")
        st.write(f"- Average comments: **{int(df['comments'].mean()):,}**")
        st.write(f"- Best engagement: **{int(df['engagement'].max()):,}**")

        st.info(
            "This is a demo dashboard for showcasing Python, Pandas, and "
            "data visualization skills. Live Instagram scraping is disabled "
            "for security and reliability."
        )
