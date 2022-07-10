import requests
import json
import tweepy
from .my_secrets import BEARER_TOKEN2

#API_URL = "https://api.twitter.com/2/tweets/440322224407314432"

#BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAG%2FIZgEAAAAAA9OgJ56Zkw3BR9s0a1geAvJifJA%3D1ae6zLaCr4noTARaHsRxSnEvEO4QUZ1KxSq7g483wAuaP2D8tI"
BEARER_TOKEN = BEARER_TOKEN2()

def search_twittor(query, tweet_fields, bearer_token):
    headers = {"Authorization":"Bearer {}".format(BEARER_TOKEN)}
    
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(query, tweet_fields)
    
    response = requests.request("GET", url, headers=headers)
    
    print("Statorse Code-o: ", response.status_code)
    
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

# query = "thye"
# tweet_fields = "tweet.fields=text,author_id,created_at"
# json_response = search_twittor(query=query, tweet_fields=tweet_fields, bearer_token=BEARER_TOKEN)
# 
# print("YUSP!", json.dumps(json_response, indent=5, sort_keys=True))
