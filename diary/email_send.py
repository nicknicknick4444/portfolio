import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment

from .email_deets import MY_ADDRESS, MY_PASSWORD, \
     HOST_ADDRESS, HOST_PORT
from .models import Entry

#listy = ["Uno", "Dos", "Tres"]

def grab_posts(USER):
    posts = Entry.objects.filter(user__exact=USER)
    listage = [i for i in posts]
    return listage

def send_email(RECIPIENT_ADDRESS, USER):
    server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
    server.starttls()
    server.login(MY_ADDRESS, MY_PASSWORD)

    #Crceation of the MIMEMultipart object
    message = MIMEMultipart()

    #Setup of MIMEMultiprt Object header
    message["From"] = MY_ADDRESS
    message["To"] = RECIPIENT_ADDRESS
    message["Subject"] = "Automated HTML Email"
    
    listy = grab_posts(USER)

    #HTML Setup
    TEMPLATE = """
        <html>
            <head></head>
            <body>
                <p style="color: orange;">This is my first HTML automated email!</p>
                <p style="color: blue;">
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

def main(USER):
    send_email("diarynotes444@gmail.com", USER)

if __name__ == "__main__":
    main(USER)

