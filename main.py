from flask import Flask,request, url_for, redirect, render_template, request
import pickle
from validate import fake_news_det as detect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from email.mime.application import MIMEApplication
import os
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)


model = pickle.load(open('model_svm.pkl','rb'))

# load_dotenv()

# sender_address = os.environ.get('GMAIL_USER') 
# sender_pass = os.environ.get('GMAIL_PASSWORD')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yoursfakely@gmail.com'
app.config['MAIL_PASSWORD'] = 'yoyomanthan987'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/', methods = ["GET","POST"])
def home():

    if request.method == "POST":
        text = request.values.get("news")
        prediction = detect(text)
        return render_template("index.html", prediction = prediction)

    return render_template("index.html")

@app.route('/alert', methods = ["GET", "POST"])
def alert():

   msg = Message('Alerted', sender = 'yoursfakely@gmail.com', recipients = ['ishitagops12@gmail.com'])
   msg.body = "The mentioned content is FAKE,Alerted the authorities!"
   mail.send(msg)
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







