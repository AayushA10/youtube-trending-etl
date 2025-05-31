# 📈 YouTube Trending Videos ETL + Dashboard

This project fetches the latest trending YouTube videos using the YouTube Data API v3, stores the data in a local SQLite database, and visualizes it with an interactive Streamlit dashboard. The data pipeline automatically updates every minute to ensure fresh insights.

## 🚀 Features

The application fetches the Top 50 trending YouTube videos, capturing key metadata like video titles, channel names, view counts, like counts, and category IDs. This data is stored in a local SQLite database for persistence. A scheduler runs in the background to update the database automatically every 1 minute. The dashboard built with Streamlit provides an interactive interface that displays all trending videos in a searchable table, bar charts highlighting the top 10 videos by views and likes, a pie chart showing the distribution by category, and allows users to filter videos by channel name.

## 🛠️ Tech Stack

This project leverages Python 3 for data extraction and database management, SQLite for lightweight local storage, and Streamlit to build the interactive dashboard. Plotly is used for creating dynamic and responsive charts, while Schedule is utilized to automate the periodic data updates.

## 📦 Installation and Setup

To set up the project locally, first clone the repository:

```bash
git clone https://github.com/AayushA10/youtube-trending-etl.git
cd youtube-trending-etl

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
# OR
venv\Scripts\activate         # Windows

Install all dependencies:
pip install -r requirements.txt

Add your YouTube Data API Key by editing the scraper.py file and replacing:

python
Copy
Edit
API_KEY = "YOUR_API_KEY_HERE"

To run the scraper and start the scheduler:
python3 scraper.py

The dashboard can be launched with:
streamlit run app.py

🎯 Future Improvements
Potential future enhancements include deploying the dashboard to Streamlit Cloud for public access, integrating a more scalable database like PostgreSQL or MongoDB, adding historical trend tracking to analyze how video rankings evolve over time, and dockerizing the application for easier deployment in different environments.
