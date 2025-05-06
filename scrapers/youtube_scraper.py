import os
import yaml
from yt_dlp import YoutubeDL
from datetime import datetime

def scrape_videos(topic_config, channel_config):
    with open(topic_config) as f:
        topics = yaml.safe_load(f)['topics']
    with open(channel_config) as f:
        channels = yaml.safe_load(f)['channels']['include']

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,
        'outtmpl': 'data/raw/%(id)s.json'
    }

    for topic in topics:
        for term in topic['search_terms']:
            print(f"Searching for: {term}")
            with YoutubeDL(ydl_opts) as ydl:
                search_url = f"ytsearchdate10:{term}"
                info = ydl.extract_info(search_url, download=False)
                for entry in info['entries']:
                    if entry['uploader_id'] in channels:
                        # Save metadata
                        filename = f"data/raw/{entry['id']}.json"
                        with open(filename, 'w', encoding='utf-8') as f:
                            yaml.dump(entry, f)
                        print(f"Saved: {entry['title']}")

if __name__ == "__main__":
    scrape_videos('config/topics.yaml', 'config/channels.yaml')