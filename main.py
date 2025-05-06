import os

def run_pipeline():
    print("Step 1: Scraping videos...")
    os.system("python scrapers/youtube_scraper.py")
    print("Step 2: Transcribing videos...")
    os.system("python processing/transcriber.py")
    print("Step 3: Sentiment analysis...")
    os.system("python processing/sentiment_analyzer.py")
    print("Step 4: Building network...")
    os.system("python analysis/network_builder.py")
    print("Pipeline complete! Run 'streamlit run visualization/web_dashboard.py' to view results.")

if __name__ == "__main__":
    run_pipeline()
