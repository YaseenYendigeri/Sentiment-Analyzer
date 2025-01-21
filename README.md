# Sentiment Analyzer

A Flask-based sentiment analyzer that uses open-source language models to provide detailed sentiment analysis for text and audio inputs. The application features a clean and responsive web interface with sentiment-specific emojis and detailed confidence scores for better user experience.

## Features

- Analyze text sentiment (positive, neutral, negative) with confidence scores.
- Analyze audio sentiment with transcription and emotion mapping.
- Visual representation of emotions with corresponding emojis.
- Simple and intuitive user interface with responsive design.

## Tech Stack

- **Backend**: Flask, Hugging Face Transformers, PyTorch, OpenAI Whisper
- **Frontend**: HTML, CSS (internal), JavaScript (vanilla)
- **Models**:
  - Text Analysis: `distilbert-base-uncased-finetuned-sst-2-english`
  - Audio Analysis: OpenAI's Whisper for transcription

## Installation and Setup

### Prerequisites

- Python 3.10+
- Virtual environment (optional but recommended)
- `pip` for package installation

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-analyzer.git
   cd sentiment-analyzer
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## API Endpoints

### Analyze Text Sentiment
- **URL**: `/analyze-text`
- **Method**: `POST`
- **Parameters**:
  - `text` (string): Text to analyze.
- **Response**:
  ```json
  {
    "sentiment": {
      "label": "positive",
      "score": 0.95
    },
    "emotions": {
      "joy": 0.8,
      "anger": 0.05
    }
  }
  ```

### Analyze Audio Sentiment
- **URL**: `/analyze-audio`
- **Method**: `POST`
- **Parameters**:
  - `audio` (file): Audio file to analyze.
- **Response**:
  ```json
  {
    "sentiment": {
      "label": "neutral",
      "score": 0.72
    },
    "emotions": {
      "calm": 0.6,
      "sadness": 0.2
    }
  }
  ```

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for feature suggestions and bug reports.
