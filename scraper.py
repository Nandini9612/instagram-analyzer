import instaloader
from dataclasses import dataclass

@dataclass
class PostData:
    shortcode: str
    date: object
    likes: int
    comments: int
    caption: str
    url: str

@dataclass
class Profile:
    username: str
    full_name: str
    biography: str
    followers: int
    following: int
    posts_count: int
    profile_pic_url: str
    posts: list

def fetch_profile(username: str, max_posts: int = 20):
    L = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        save_metadata=False,
    )

    profile = instaloader.Profile.from_username(L.context, username)

    posts = []
    count = 0

    for post in profile.get_posts():
        if count >= max_posts:
            break

        real_shortcode = post.shortcode  # ✅ REAL shortcode from Instagram
        real_url = f"https://www.instagram.com/p/{real_shortcode}/"

        posts.append(PostData(
            shortcode=real_shortcode,
            date=post.date_utc,
            likes=int(post.likes),
            comments=int(post.comments),
            caption=post.caption if post.caption else "",
            url=real_url
        ))
        count += 1

    return Profile(
        username=profile.username,
        full_name=profile.full_name,
        biography=profile.biography,
        followers=int(profile.followers),
        following=int(profile.followees),
        posts_count=int(profile.mediacount),
        profile_pic_url=str(profile.profile_pic_url),
        posts=posts
    )
