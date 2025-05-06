from transformers import pipeline
import os

def analyze_sentiment(text, lang='en'):
    if lang == 'en':
        classifier = pipeline("sentiment-analysis")
    else:
        classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    return classifier(text[:512])[0]  # Truncate for demo

def batch_analyze():
    for file in os.listdir('data/processed'):
        if file.endswith('_transcript.txt'):
            with open(f"data/processed/{file}", encoding='utf-8') as f:
                text = f.read()
            sentiment = analyze_sentiment(text)
            with open(f"data/processed/{file.replace('_transcript.txt', '_sentiment.yaml')}", 'w') as f:
                import yaml
                yaml.dump(sentiment, f)
            print(f"Analyzed sentiment for {file}")

if __name__ == "__main__":
    batch_analyze()
