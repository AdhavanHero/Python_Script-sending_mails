import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

api_key = os.environ.get('Api_key')
email = os.environ.get('Email')

# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = email
smtp_password = api_key

def messages(Var1, Var2, Var3):
    message = MIMEMultipart()
    message["From"] = email
    message["To"] = Var2
    message["Subject"] = Var1
    message_text = Var3
    message.attach(MIMEText(message_text))

    smtp_client = smtplib.SMTP(smtp_server, smtp_port)
    smtp_client.ehlo()
    smtp_client.starttls()
    smtp_client.login(smtp_username,smtp_password)
    smtp_client.sendmail(message["From"], message["To"], message.as_string())
    smtp_client.quit() 

my_array = [
    {"email": "ap4992@srmist.edu.in", "Cont": "Hi dude", "mission": "save the world"},
    {"email": "adhavanponram@gmail.com", "Cont": "Hi Adhavan", "mission": "Never give up"},
    {"email": "Superhero8871@gmail.com", "Cont": "Hi Hero", "mission": "win the war at any cost"}
]

for item in my_array:
    messages(item["mission"], item["email"], item["Cont"])
    
print('Array printed!')    




