import streamlit as st
import matplotlib.pyplot as plt
from src.scraper import fetch_profile
from src.analyzer import analyze_profile

st.set_page_config(page_title="Instagram Live Profile Analyzer", layout="wide")
st.title("📊 Instagram Live Profile Analyzer")

username = st.text_input("Enter Instagram Username (public only, no @)")

if st.button("Analyze"):
    if not username.strip():
        st.error("Please enter a username.")
    else:
        with st.spinner("Fetching LIVE Instagram data..."):
            profile = fetch_profile(username.strip())
            metrics = analyze_profile(profile)

        st.success("Live analysis completed ✅")

        # -------- PROFILE INFO --------
        st.subheader("📌 Profile Info")
        col1, col2 = st.columns(2)

        with col1:
            st.write("Username:", metrics["username"])
            st.write("Full Name:", metrics["full_name"])
            st.write("Followers:", metrics["followers"])
            st.write("Following:", metrics["following"])
            st.write("Total Posts:", metrics["posts_count"])

        with col2:
            st.write("Biography:")
            st.info(metrics["biography"])

        # -------- AVERAGE ENGAGEMENT --------
        st.subheader("📊 Average Engagement")
        st.write("Avg Likes:", metrics["avg_likes"])
        st.write("Avg Comments:", metrics["avg_comments"])
        st.write("Avg Engagement:", metrics["avg_engagement"])

        # -------- DATAFRAME --------
        df = metrics["posts_df"]     # ✅ df is defined HERE
        df_sorted = df.sort_values("date")

        st.subheader("📝 Recent Posts Data")
        st.dataframe(df_sorted[["date", "likes", "comments", "engagement", "url"]])

        # -------- CHART 1 --------
        st.subheader("📈 Likes per Post")
        fig1 = plt.figure()
        plt.plot(df_sorted["likes"].values)
        plt.xlabel("Post Index")
        plt.ylabel("Likes")
        plt.title("Likes per Post")
        st.pyplot(fig1)
        plt.clf()

        # -------- CHART 2 --------
        st.subheader("📉 Engagement per Post")
        fig2 = plt.figure()
        plt.plot(df_sorted["engagement"].values)
        plt.xlabel("Post Index")
        plt.ylabel("Engagement")
        plt.title("Engagement per Post")
        st.pyplot(fig2)
        plt.clf()

        # -------- HASHTAGS --------
        st.subheader("🔥 Top Hashtags")
        for tag, count in metrics["top_hashtags"]:
            st.write(f"{tag} → {count}")
