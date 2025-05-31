import requests
import pandas as pd
import sqlite3
import schedule
import time

API_KEY = "AIzaSyBpdTzynRzgKwrJcN8XzNCZvsixllpNGX4"

TRENDING_URL = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode=US&maxResults=50&key={API_KEY}"

def fetch_trending_videos():
    response = requests.get(TRENDING_URL)
    data = response.json()

    if 'items' not in data:
        raise Exception(f"Error in API response: {data}")

    videos = []
    for item in data['items']:
        video = {
            'video_id': item['id'],
            'title': item['snippet']['title'],
            'channel_title': item['snippet']['channelTitle'],
            'category_id': item['snippet']['categoryId'],
            'view_count': item['statistics'].get('viewCount', 0),
            'like_count': item['statistics'].get('likeCount', 0)
        }
        videos.append(video)

    return pd.DataFrame(videos)

def save_to_db(df):
    conn = sqlite3.connect('youtube_trending.db')
    df.to_sql('trending_videos', conn, if_exists='replace', index=False)
    conn.close()

def job():
    print("📈 Fetching latest trending videos...")
    try:
        df = fetch_trending_videos()
        save_to_db(df)
        print("✅ Data updated successfully!")
    except Exception as e:
        print("❌ Error while updating data:", e)

if __name__ == "__main__":
    # Har 1 minute me update karega
    schedule.every(1).minutes.do(job)

    print("Scheduler Started... Updating every 1 minute ⏳")
    while True:
        schedule.run_pending()
        time.sleep(1)
