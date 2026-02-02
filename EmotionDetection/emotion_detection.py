import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector2(text_to_analyse):  # Define a function named that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the analysis service
    input_json = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = input_json, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = response.json() # Parsing the JSON response from the API
    if response.status_code == 200:
        emoti= formatted_response['emotionPredictions'][0] # looking for only emotions
        emoti1= emoti['emotion'] # These are the emotion-score pairs we are looking for
        dominant= max(emoti1, key=emoti1.get) # looking for highest score
    elif response.status_code == 400:
        emoti1 = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None}
        dominant = None
 

    return {
    'anger': emoti1['anger'],
    'disgust': emoti1['disgust'],
    'fear': emoti1['fear'],
    'joy': emoti1['joy'],
    'sadness': emoti1['sadness'],
    'dominant_emotion': dominant
}  # Return the correct answer