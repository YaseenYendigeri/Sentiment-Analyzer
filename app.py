from flask import Flask, render_template, request, jsonify
from models.text_model import analyze_sentiment
from models.voice_model import analyze_voice_sentiment
from models.emotion_model import analyze_emotions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze-text", methods=["POST"])
def analyze_text():
    text = request.form["text"]
    sentiment_results = analyze_sentiment(text)
    emotion_results = analyze_emotions(text)

    return jsonify({
        "sentiment": sentiment_results,
        "emotions": emotion_results
    })

@app.route("/analyze-audio", methods=["POST"])
def analyze_audio():
    audio = request.files["audio"]
    audio.save("temp_audio.wav")
    transcription_results = analyze_voice_sentiment("temp_audio.wav")

    text = transcription_results["transcription"]
    sentiment_results = analyze_sentiment(text)
    emotion_results = analyze_emotions(text)

    return jsonify({
        "transcription": transcription_results,
        "sentiment": sentiment_results,
        "emotions": emotion_results
    })

if __name__ == "__main__":
    app.run(debug=True)
