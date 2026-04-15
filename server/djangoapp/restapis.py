import requests
import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

backend_url = os.getenv('backend_url', default="http://127.0.0.1:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://127.0.0.1:5050/")


def get_request(endpoint, **kwargs):
    params = {}
    if kwargs:
        params = kwargs
    response = requests.get(f"{backend_url}/{endpoint}", params=params)
    return response.json()

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + quote(text)
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")