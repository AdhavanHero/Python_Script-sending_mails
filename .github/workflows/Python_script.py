import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

api_key = os.environ.get('Api_key')
email = os.environ.get('Email')

print(api_key)
Print(email)


