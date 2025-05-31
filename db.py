import sqlite3
import pandas as pd

def load_data():
    conn = sqlite3.connect('youtube_trending.db')
    df = pd.read_sql('SELECT * FROM trending_videos', conn)
    conn.close()
    return df
