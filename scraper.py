import random
from datetime import datetime, timedelta

def fetch_profile(username):
    return {
        "username": username,
        "full_name": "Demo User",
        "bio": "This is demo data for safe public deployment.",
        "followers": random.randint(1000, 100000),
        "following": random.randint(100, 5000),
        "posts": random.randint(50, 500)
    }

def fetch_posts(username):
    posts = []
    for i in range(10):
        posts.append({
            "date": datetime.now() - timedelta(days=i),
            "likes": random.randint(100, 5000),
            "comments": random.randint(5, 300),
            "engagement": random.randint(150, 5500),
            "url": "https://www.instagram.com/"
        })
    return posts
