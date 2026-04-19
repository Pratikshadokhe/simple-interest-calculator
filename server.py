from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect():
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}. "
        f"Dominant emotion: {result['dominant_emotion']}"
    )

@app.route("/")
def home():
    return "Emotion Detector Running!"

if __name__ == "__main__":
    app.run(debug=True)
