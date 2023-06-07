import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

email = os.environ.get('Email')
api_key = os.environ.get('Api_key')
print(email)
print(api_key)

