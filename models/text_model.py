from transformers import pipeline

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    """
    Analyze sentiment with detailed scores.
    """
    results = sentiment_pipeline(text, return_all_scores=True)
    return results
