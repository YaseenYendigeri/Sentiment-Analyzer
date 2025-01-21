import moviepy.editor as mp
from models.voice_model import analyze_voice_sentiment

def analyze_video_sentiment(filepath):
    video = mp.VideoFileClip(filepath)
    audio_path = filepath.replace('.mp4', '.wav')
    video.audio.write_audiofile(audio_path)
    sentiment = analyze_voice_sentiment(audio_path)
    return sentiment
