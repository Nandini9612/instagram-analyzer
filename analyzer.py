import pandas as pd
from collections import Counter

def analyze_profile(profile):
    rows = []

    for post in profile.posts:
        rows.append({
            "shortcode": post.shortcode,
            "date": post.date,
            "likes": post.likes,
            "comments": post.comments,
            "engagement": post.likes + post.comments,
            "caption": post.caption,
            "url": post.url
        })

    df = pd.DataFrame(rows)

    metrics = {
    "username": profile.username,
    "full_name": profile.full_name,        # ✅ ADDED
    "biography": profile.biography,        # ✅ ADDED
    "followers": profile.followers,
    "following": profile.following,
    "posts_count": profile.posts_count,
    "avg_likes": int(df["likes"].mean()),
    "avg_comments": int(df["comments"].mean()),
    "avg_engagement": float(df["engagement"].mean()),
    "posts_df": df
}


    hashtags = Counter()
    for caption in df["caption"]:
        for word in caption.split():
            if word.startswith("#"):
                hashtags[word.lower()] += 1

    metrics["top_hashtags"] = hashtags.most_common(10)
    return metrics
