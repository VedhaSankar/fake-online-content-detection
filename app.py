from flask import Flask,request, url_for, redirect, render_template, request
import pickle
from score import predict_link_score as detect_link
from score import predict_content_score as detect_content
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

# https://www.dnaindia.com/education/report-cbse-class-10-12-board-exam-2022-term-1-cancellation-latest-updates-news-exam-centre-datesheetonline-petition-2917207
# https://www.bbc.com/news/live/world-europe-60685883


model = pickle.load(open('model_svm.pkl','rb'))

load_dotenv()

# SENDER_ADDRESS = os.environ.get('GMAIL_USER') 
# SENDER_PASS = os.environ.get('GMAIL_PASSWORD')

SENDER_ADDRESS  = os.environ.get('GMAIL_USER') 
SENDER_PASS     = os.environ.get('GMAIL_PASSWORD')
EMAIL_LIST      = os.environ.get('EMAIL_LIST').split(',')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = SENDER_ADDRESS
app.config['MAIL_PASSWORD'] = SENDER_PASS
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
            print("Prediction: ", prediction)        

        except:
            pass
        return render_template("index.html", prediction = prediction)

    return render_template("index.html")

@app.route('/alert', methods = ["GET", "POST"])
def alert():

    for sender in EMAIL_LIST:
        send_email(
            receiver_address=sender,
            subject='Alert',
            content="The mentioned content is FAKE, alerted the authorities!!"
            )

    return render_template("index.html")

if __name__ == "__main__":

    app.run(debug = True,host="0.0.0.0", port = 8500)







