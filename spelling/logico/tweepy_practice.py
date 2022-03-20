import random, ast
import datetime
import tweepy

from ..models import Admonish, TweetLists


client = tweepy.Client(
consumer_key = "SECRET",
consumer_secret = "SECRET",
access_token = "SECRET",
access_token_secret = "SECRET",
)

auth = tweepy.OAuth1UserHandler(
    client.consumer_key, client.consumer_secret, client.access_token, client.access_token_secret
    )

api = tweepy.API(auth)

words = ["againts", "alwyas", "becasue", "firend", "realyl", "thye"]

def cookie_help(reqc, tok, func):
    if not tok in reqc:
        vari = reqc.get(tok, func)
        return vari
    else:
        vari = reqc[str(tok)]
        return vari

def cookie_help_2(recq, tok, func, elso):
    if not tok in recq:
        vari = recq.get(tok, func)
        return vari
    else:
        vari = elso
        return vari

def page_turn(gus, whichp, dicty2):
    if int(gus) > 6:
        gus = "6"
        whichp = "26 - 30"
    if int(gus) < 1:
        gus = "1"
        whichp = "1 - 5"
    if gus == "1":
        dicty2 = dicty2[:5]
        whichp = "1 - 5"
    elif gus == "2":
        dicty2 = dicty2[5:10]
        whichp = "6 - 10"
    elif gus == "3":
        dicty2 = dicty2[10:15]
        whichp = "11 - 15"
    elif gus == "4":
        dicty2 = dicty2[15:20]
        whichp = "16 - 20"
    elif gus == "5":
        dicty2 = dicty2[20:25]
        whichp = "21 - 25"
    elif gus == "6":
        dicty2 = dicty2[25:30]
        whichp = "26 - 30"
    return dicty2, whichp

def getty(search_term):
    tweets = api.search_tweets(q=search_term, count=300, tweet_mode="extended")
    
    those_tweets = []
    for tweet in tweets:
        ind_tweet = {}
        goose = tweet
        ind_tweet["their_username"] = goose._json["user"]["screen_name"]
        ind_tweet["tweet_text"] = goose._json["full_text"]
        ind_tweet["tweet_id"] = goose._json["id_str"]
        raw_date = goose._json["created_at"].replace("+0000 ", "")
        date_half1 = str(raw_date[:10])
        date_half2 = str(raw_date[10:-5])
        
        ind_tweet["tweet_date"] = date_half1 + " " + str(datetime.datetime.now().year) + " - " + date_half2

        those_tweets.append(ind_tweet)
    those_tweets2 = [i for i in those_tweets if i["tweet_text"][:4] != "RT @"]
    those_tweets2 = those_tweets2[:30]
    
    print("If you see this, the tweets are being (re)generated!!!!!!!!!!!")
    return those_tweets2

def make_lists(seshn):
    global words
    for term in words:
        big_list = getty(term)
        if not TweetLists.objects.filter(twe_term=term, twe_seshn=seshn).exists():
            db = TweetLists.objects.create(twe_dict = big_list, twe_term = term, \
                                           twe_seshn=seshn, twe_time = datetime.datetime.now())
            db.save()

def get_lists(term, seshn):
    word_dict = TweetLists.objects.filter(twe_seshn = seshn, twe_term=term).values_list("twe_dict")
    word_dict = word_dict[0][0]
    word_dict = str(word_dict)[1:-2] + "}"
    word_dict = ast.literal_eval(word_dict)
    return word_dict

def send_tweet(word, that_id):
    return api.update_status(status=word, in_reply_to_status_id=that_id, auto_populate_reply_metadata=True)

def make_id():
    cooko = random.randint(100000000000000000000,999999999999999999999)
    return str(cooko) + "BASP"

def get_answers():
    global words
    ids = [random.randint(1,2) for i in range(1,len(words)+1)]
    your_words = dict(zip(words, ids))
    print("PRADDLE", your_words)
    return your_words

def lookup_answer(the_id, wordu):
    answer = str(Admonish.objects.filter(adm_id=the_id, adm_term=wordu)[0])
    return answer

def readie(raw):
    raw = raw.replace("\054", ",").replace("\"","")
    raw = ast.literal_eval(raw)
    print("DICT?",raw)
    return raw

