import smtplib
#import schedule
import time
import datetime as datetime_module
from datetime import datetime as date_for_str
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment

from .email_deets import MY_ADDRESS, MY_PASSWORD, HOST_ADDRESS, HOST_PORT
from .models import Entry, User, SendTime
#from .service import convert_date2 as convert_date3
#from .service import today as today2

#listy = ["Uno", "Dos", "Tres"]

# def emailer():
#     print("I'M A-WORKING!")


def today2():
    return datetime_module.datetime.now().date()

def convert_date2(d):
    print("PORTY!", d, type(d))
    converted = d.strftime("%d/%m/%Y")
    print(converted)
    return converted

def grab_posts(USER):
    if Entry.objects.filter(user__exact=USER, date_for__exact=today2()).exists():
        posts = Entry.objects.filter(user__exact=USER, date_for__exact=today2()).order_by("title", "detail")
        listage = [i for i in posts]
    else:
        listage = [["BLANK"]]
    return listage

def send_email():
    
    server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
    server.starttls()
    server.login(MY_ADDRESS, MY_PASSWORD)
    
    user_que = User.objects.values_list("first_name", "email")
    USERS = [i for i in user_que]
    
    for i in USERS:
        curr_user = i[0]
        curr_day = today2()
        str_day_raw = date_for_str.now()
        
        day_str = convert_date2(str_day_raw)
        sd_abbrev = day_str[:5]
        
        ### Hide this and re-add as func arg for test sending
        RECIPIENT_ADDRESS = i[1]
        
        #Creation of the MIMEMultipart object
        message = MIMEMultipart()

        #Setup of MIMEMultiprt Object header
        message["From"] = MY_ADDRESS
        message["To"] = RECIPIENT_ADDRESS
        message["Subject"] = f"Diary Notes for {curr_user} ({day_str})"
        
        listy = grab_posts(i[0])
        lengtho = len(listy)
        user_list = []
        if listy[0] != ["BLANK"]:
            for index, order in enumerate(listy):
                if index > 0 and listy[index].title[0] != listy[index-1].title[0]:
                    user_list.append(["&nbsp;", "&nbsp;"])
                    user_list.append([order.title + "&nbsp;-&nbsp;", order.detail])
                else:
                    user_list.append([order.title + "&nbsp;-&nbsp;", order.detail])
        else:
            user_list.append(["BLANK", "BLANK"])
        
        #HTML Setup
        TEMPLATE = """
            <html>
                <head></head>
                <body>
                    <p style="color: #000000;">
                    <b><u>Diary Notes for {{ curr_user }}:</u></b><br><br>
                    
                      {% if user_list.0.0 == "BLANK" %}
                        No diary notes today!<br>
                          
                      {% else %}
                      Good morning,
                      
                      {% if user_list.0.0 != "BLANK" and lengtho == 1 %}
                        <p>Here is your diary note for {{ sd_abbrev }}:<br><br></p>
                    
                      {% else %}
                        <p>Here are your diary notes for {{ sd_abbrev }}:<br><br></p>
                      {% endif %}
                      
                       {% for item in user_list %}

                       <span style="font-size: 15px;">{{ item.0 }}{{ item.1 }}</span><br>
                     
                     
                       {% endfor %}
                      <br>
                      {% endif %}
                    
                    
                    <p>All the best,</p>
                    <p>Nick</p>
                 </p>
                </body>
            </html>
        """

        
        
        #Creation of a MIMEText Part
        #htmlPart = MIMEText(html, "html")
        htmlPart = MIMEText(
            Environment().from_string(TEMPLATE).render(
                    listy = listy, user_list = user_list, \
                    curr_user = curr_user, day_str = day_str, \
                    sd_abbrev = sd_abbrev, lengtho = lengtho
                ),"html"
            )

        #Part attachment
        message.attach(htmlPart)

        #Send email and close connection
        server.send_message(message)
        # END!
            
    server.quit()
    
    print("CHECK EMAIL!")
    
def main():
    # Re-dd email address for testing
    send_email()
    #for_dry_runs()

if __name__ == "__main__":
    main()

