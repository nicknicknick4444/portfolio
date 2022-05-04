import datetime, smtplib
from datetime import datetime as date_for_str
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment

from .email_deets import MY_ADDRESS, MY_PASSWORD, \
     HOST_ADDRESS, HOST_PORT
from .models import Entry, User
from .service import today, convert_date2

#listy = ["Uno", "Dos", "Tres"]

def grab_posts(USER):
    if Entry.objects.filter(user__exact=USER, date_for__exact=today()).exists():
        posts = Entry.objects.filter(user__exact=USER, date_for__exact=today()).order_by("title", "detail")
        listage = [i for i in posts]
    else:
        listage = [["BLANK"]]
    return listage


def send_email(RECIPIENT_ADDRESS):
    
    server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
    server.starttls()
    server.login(MY_ADDRESS, MY_PASSWORD)
    
    user_que = User.objects.values_list("first_name", "email")
    USERS = [i for i in user_que]
    print(USERS)
    
    for i in USERS:
        # TO SEND TO ALL USERS AGAIN REMOVE THIS IF LOOP WHEN FINISHED AND JUDD EVERYTHING UP TO BISMARK BACK 1 DENT
        print(i)
        if i[0] == "Nick" or i[0] == "Prady":
            curr_user = i[0]
            curr_day = today()
            str_day = date_for_str.now()
            day_str = convert_date2(str_day)
            print("BAGS!", day_str)
            ####RECIPIENT_ADDRESS = i[1]
            
            #Creation of the MIMEMultipart object
            message = MIMEMultipart()

            #Setup of MIMEMultiprt Object header
            message["From"] = MY_ADDRESS
            message["To"] = RECIPIENT_ADDRESS
            #message["To"] = i[1]
            message["Subject"] = f"Diary Notes for {curr_user} ({day_str})"
            
            listy = grab_posts(i[0])
            print(listy[0], type(listy[0]))
            user_list = []
            if listy[0] != ["BLANK"]:
                for index, order in enumerate(listy):
                    if index > 0 and listy[index].title[0] != listy[index-1].title[0]:
                        user_list.append(["&nbsp;", "&nbsp;"])
                        user_list.append([order.title + "&nbsp;-&nbsp;", order.detail])
                    else:
                        #for i in ordo:
                        user_list.append([order.title + "&nbsp;-&nbsp;", order.detail])
                        #print(ordo.title, index, print(type(ordo)))
                print(user_list)
            else:
                user_list.append(["BLANK", "BLANK"])
            
            #HTML Setup
            TEMPLATE = """
                <html>
                    <head></head>
                    <body>
                        <p style="color: #000000;">
                        <b><u>Diary Notes for {{ curr_user }}:</u></b><br><br>
                        {% for item in user_list %}
                          {% if item.0 == "BLANK" %}
                            No diary notes today!<br>
                          {% else %}
                           {{ item.0 }}{{ item.1 }}<br>
                         
                         
                         
                          {% endif %}
                        {% endfor %}
                        </p>
                        <p>All the best,</p>
                        <p>Nick</p>
                    </body>
                </html>
            """

            

            #Creation of a MIMEText Part
            #htmlPart = MIMEText(html, "html")
            htmlPart = MIMEText(
                Environment().from_string(TEMPLATE).render(
                        listy = listy, user_list = user_list, \
                        curr_user = curr_user, str_day = str_day
                    ),"html"
                )

            #Part attachment
            message.attach(htmlPart)

            #Send email and close connection
            server.send_message(message)
            # BISMARK!
            
    server.quit()
    
    print("CHECK EMAIL!")
    
    
def timer():
    #convert_date2(date_for_str.now())
    return send_email("diarynotes444@gmail.com")

def main():
    #send_email("diarynotes444@gmail.com")
    timer()

if __name__ == "__main__":
    main()

