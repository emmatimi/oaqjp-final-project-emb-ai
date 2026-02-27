import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(URL, json = myobj, headers = header)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    """Converting the string into a dictionary"""
    formatted_response = json.loads(response.text)
    
    """Extract the specific emotions"""
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion['anger']
    disgust_score = emotion['disgust']
    fear_score = emotion['fear']
    joy_score = emotion['joy']
    sadness_score = emotion['sadness']

    """list for finding the dominant emotion"""
    emotion_list = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    """Find the dominant emotion"""
    dominant_emotion = max(emotion_list, key = emotion_list.get)
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }