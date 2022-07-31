from .logico.tweepy_process import getty

def getto(search_term):
    return getty(search_term)

def cleanup(reqc, reso):
    mainlist = ["cou", "startytime", "finishy_time", "excepor", "resety", \
                "squores", "goesy", "query_s", "query_u", "query_d", "design", "picked_colour", \
                "sum_list", "colours_list"]
    for i in mainlist:
        if i in reqc.COOKIES:
            reso.delete_cookie(i)
