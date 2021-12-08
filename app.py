from flask import Flask,request, url_for, redirect, render_template, request
import pickle
from validate import fake_news_det as detect_content
from newspaper_test import detect_link
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from email.mime.application import MIMEApplication
import os
from flask_mail import Mail, Message
from emailer import send_email

app = Flask(__name__)
mail= Mail(app)


model = pickle.load(open('model_svm.pkl','rb'))

# load_dotenv()

# sender_address = os.environ.get('GMAIL_USER') 
# sender_pass = os.environ.get('GMAIL_PASSWORD')

sender_address = os.environ.get('GMAIL_USER') 
sender_pass = os.environ.get('GMAIL_PASSWORD')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = sender_address
app.config['MAIL_PASSWORD'] = sender_pass
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/', methods = ["GET","POST"])
def home():

    if request.method == "POST":
        try:
            content = request.values.get("news_content")
            prediction = detect_content(content)
        except:
            pass
        try:
            link = request.values.get("news_link")
            prediction = detect_link(link)
        except:
            pass
        
        return render_template("index.html", prediction = prediction)

    return render_template("index.html")

@app.route('/alert', methods = ["GET", "POST"])
def alert():

    email_list = ['vedhasankar26@gmail.com', "harenemaharajan02@gmail.com", "ishitagops12@gmail.com"]

    for sender in email_list:
        send_email(
            receiver_address=sender,
            subject='Hail Hydra',
            content="pakka spam maddri irukku pt 2"
            )
    # msg = Message('Alerted', sender = 'yoursfakely@gmail.com', recipients = ['ishitagops12@gmail.com'])
    # msg.body = "The mentioned content is FAKE,Alerted the authorities!"
    # mail.send(msg)
    return render_template("index.html")


# @app.route('/predict', methods = ["GET","POST"])
# def send_content():
#     # text = request.values.get("news")

#     # prediction = detect(text)
#     prediction = "hello"
#     # return render_template("index.html", prediction = prediction)
#     return redirect(url_for('home'))

if __name__ == "__main__":

    app.run(debug = True,host="0.0.0.0")







