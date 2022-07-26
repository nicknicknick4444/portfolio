import requests
import json
import tweepy
from .my_secrets import BEARER_TOKEN2

BEARER_TOKEN = BEARER_TOKEN2()

def search_twittor(query, tweet_fields, bearer_token):
    headers = {"Authorization":"Bearer {}".format(BEARER_TOKEN)}
    
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(query, tweet_fields)
    
    response = requests.request("GET", url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

