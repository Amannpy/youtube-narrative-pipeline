import os
from youtube_transcript_api import YouTubeTranscriptApi
import whisper

def transcribe_video(video_id, lang='en'):
    try:
        # Try YouTube transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        return " ".join([x['text'] for x in transcript])
    except Exception:
        # Fallback to Whisper
        model = whisper.load_model("base")
        audio_path = f"data/raw/{video_id}.mp3"
        # Download audio using yt-dlp
        os.system(f"yt-dlp -x --audio-format mp3 -o {audio_path} https://www.youtube.com/watch?v={video_id}")
        result = model.transcribe(audio_path)
        return result['text']

def batch_transcribe():
    for file in os.listdir('data/raw'):
        if file.endswith('.json'):
            video_id = file.replace('.json', '')
            transcript = transcribe_video(video_id)
            with open(f"data/processed/{video_id}_transcript.txt", 'w', encoding='utf-8') as f:
                f.write(transcript)
            print(f"Transcribed {video_id}")

if __name__ == "__main__":
    batch_transcribe()
