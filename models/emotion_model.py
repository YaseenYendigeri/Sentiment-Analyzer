from transformers import pipeline

# Load emotion detection model
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

def analyze_emotions(text):
    """
    Analyze emotions in the given text.
    """
    results = emotion_pipeline(text)
    return results
