
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from email.mime.application import MIMEApplication
import os
from os.path import basename

load_dotenv()

sender_address = os.environ.get('GMAIL_USER') 
sender_pass = os.environ.get('GMAIL_PASSWORD')

def send_email(receiver_address,subject,content):

    mail_content = content

    message = MIMEMultipart()

    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject

    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    print('Mail Sent')