import whisper

# Load Whisper model
model = whisper.load_model("base")

def analyze_voice_sentiment(audio_file_path):
    """
    Transcribe audio and return text with confidence.
    """
    result = model.transcribe(audio_file_path)
    return {
        "transcription": result["text"],
        "confidence": result.get("confidence", "N/A")
    }
