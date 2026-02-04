"""Flask server for the Emotion Detector app."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector2
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emo_det():
    """Analyze text and return emotion scores + dominant emotion."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the function and store the response
    response = emotion_detector2(text_to_analyze)

    # Extract the values from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']
    # Return a formatted string with the answer
    if anger is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant}</b>."
        )

@app.route("/")
def render_index_page():
    """Render the homepage."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
