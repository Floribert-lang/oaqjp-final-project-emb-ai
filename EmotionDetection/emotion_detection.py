import requests  # Importing the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # function that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = {"raw_document": {"text": text_to_analyse}}  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json=myobj, headers=header)  # Send a POST request to the API
    if response.status_code == 500:
        # Return a dictionary with all values as None
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    result = json.loads(response.text)  # Parse the response as JSON
    emotions = result['emotionPredictions'][0]['emotion']  # Extract the emotions dictionary

    # Identify the dominant emotion (emotion with the highest score)
    dominant_emotion = max(emotions, key=emotions.get)

    # Prepare the final output format
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return output
