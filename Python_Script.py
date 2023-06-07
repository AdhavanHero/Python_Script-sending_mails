import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

email = os.environ.get('EMAIL')
api_key = os.environ.get('API_KEY')
print(email)
print(api_key)

