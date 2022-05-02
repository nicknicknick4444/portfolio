import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment

from .email_deets import MY_ADDRESS, MY_PASSWORD, \
     HOST_ADDRESS, HOST_PORT
from .models import Entry, User

#listy = ["Uno", "Dos", "Tres"]

def grab_posts(USER):
    posts = Entry.objects.filter(user__exact=USER).order_by("title", "detail")
    listage = [i for i in posts]
    return listage

def send_email(RECIPIENT_ADDRESS):
    server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
    server.starttls()
    server.login(MY_ADDRESS, MY_PASSWORD)
    
    
    
    user_que = User.objects.values_list("first_name", "email")
    USERS = [i for i in user_que]
    print(USERS)
    
    
    for i in USERS:
    
        #Creation of the MIMEMultipart object
        message = MIMEMultipart()

        #Setup of MIMEMultiprt Object header
        message["From"] = MY_ADDRESS
        message["To"] = RECIPIENT_ADDRESS
        #message["To"] = i[1]
        message["Subject"] = f"Diary Notes for {i[0]}"
        
        listy = grab_posts(i[0])
        
        #HTML Setup
        TEMPLATE = """
            <html>
                <head></head>
                <body>
                    <p style="color: #000000;">
                    <b><u>Diary notes for {{ listy.0.user }}</u></b><br><br>
                    {% for i in listy %}
                    {{ i.title }}<br>
                    {{ i.detail }}<br><br>
                    {% endfor %}
                    </p>
                    <p>Nick</p>
                </body>
            </html>
        """

        #Creation of a MIMEText Part
        #htmlPart = MIMEText(html, "html")
        htmlPart = MIMEText(
            Environment().from_string(TEMPLATE).render(
                    listy = listy
                ),"html"
            )

        #Part attachment
        message.attach(htmlPart)

        #Send email and close connection
        server.send_message(message)
    server.quit()

    print("CHECK EMAIL!")

def main():
    send_email("richard.hart4@nhs.net")

if __name__ == "__main__":
    main()

