#from .logico.spelling_logic import search_twittor
from .logico.tweepy_practice2 import getty

# def search_twitter(query, tweet_fields, bearer_token):
#     return search_twittor

def getto(search_term):
    return getty(search_term)

dicty2u = [{'created_at': '2022-02-27T21:36:29.000Z', 'id': '1498049422680231936', 'text': '@bauhhmbo @y4ntaoist thye r so pretty', 'author_id': '1224502917249433600'},
         {'created_at': '2022-02-27T21:34:40.000Z', 'id': '1498048966553866241', 'text': '@Sindhiest Shabas athao. Beehi beehi motti ayo. 2 clock thye ahin. 😉😂', 'author_id': '613393242'},
         {'created_at': '2022-02-27T21:25:50.000Z', 'id': '1498046741584748547', 'text': "@crypto Sanctions is just official but it doesn't effect actually because thye have best solutions that you ever think.", 'author_id': '2503690909'},
         {'created_at': '2022-02-27T21:16:58.000Z', 'id': '1498044513146781703', 'text': "quite a few comments calling madea drag, and honestly i can see it. had it not been for his films pandering to conservative black folks and misogynoir, thye'd be some neat drag films https://t.co/CRx05HbrKP", 'author_id': '1278405447352016897'},
         {'created_at': '2022-02-27T20:52:57.000Z', 'id': '1498038467489513476', 'text': 'RT @eyebaIIing: THYE ALAN FANCAM IS REAL *BANGING POTS AND PANS* https://t.co/uA9UoYfbcx', 'author_id': '1252323067499393025'},
         {'created_at': '2022-02-27T20:38:47.000Z', 'id': '1498034901983113229', 'text': 'Probably the saddest part about the whole Ukraine - Russia thing is that Ukraine is naive towards the fact that thye are an infantry army and Russia is a hig tech super army. #RussiaInvadesUkraine', 'author_id': '260196527'},
         {'created_at': '2022-02-27T20:19:43.000Z', 'id': '1498030102663233536', 'text': 'THye telel mei Cantdirnk paint....litlel dothye know...i wiwl anywyas!', 'author_id': '1368768259869310979'},
         {'created_at': '2022-02-27T20:04:35.000Z', 'id': '1498026295430721540', 'text': '@Stickz____ You forgot the fact that thye dont unpdate there games', 'author_id': '1452407676764409856'},
         {'created_at': '2022-02-27T20:00:12.000Z', 'id': '1498025194132324362', 'text': '@verdanturf THYE HAVE LIPS', 'author_id': '715996464888082434'},
         {'created_at': '2022-02-27T19:39:04.000Z', 'id': '1498019872692965378', 'text': 'RT @its__kaaty: send halppp, thye are too cute @sotk_nft https://t.co/DZgIUZYPr3', 'author_id': '1347334908310679552'}]

def cleanup(reqc, reso):
    mainlist = ["sesho", "cou", "startytime", "finishy_time", "excepor", "resety", \
                "squores", "goesy", "query_s", "query_u", "query_d"]
    for i in mainlist:
        if i in reqc.COOKIES:
            reso.delete_cookie(i)
    