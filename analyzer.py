import pandas as pd

def analyze_posts(posts):
    data = []

    for post in posts:
        engagement = post.likes + post.comments
        data.append({
            "date": post.date,
            "likes": post.likes,
            "comments": post.comments,
            "engagement": engagement,
            "url": post.url
        })

    df = pd.DataFrame(data)
    return df
