# Emotion Detector Project

## 📌 Project Description
This project is an AI-based Emotion Detection Web Application built using Python and Flask. It analyzes user input text and detects emotions such as joy, anger, fear, disgust, and sadness.

## ⚙️ Technologies Used
- Python
- Flask
- Requests Library
- Watson NLP API (with fallback handling)

## 📁 Project Structure
emotion-detector/
│── emotion_detection.py
│── server.py
│── test_emotion_detection.py
│── EmotionDetection/
│   └── __init__.py

## ▶️ How to Run

### 1. Install dependencies
pip install requests flask

### 2. Run Flask server
python server.py

### 3. Open browser
http://127.0.0.1:5000/emotionDetector?textToAnalyze=I%20am%20happy

## 🧪 Running Tests
python test_emotion_detection.py

## 📊 Features
- Emotion detection using NLP
- Error handling for invalid input
- Flask web interface
- Unit testing support
- Static code analysis (pylint)

## 📸 Screenshots
- Deployment test screenshot
- Error handling screenshot
