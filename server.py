"""
This module initiates the Flask application for emotion detection.
It provides endpoints to analyze text and render the web interface.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Retrieves user text, processes it through the emotion detector, 
    and returns a formatted string with results or an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Check for invalid input/nonsense cases
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format and return the response string
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index page for the web application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    