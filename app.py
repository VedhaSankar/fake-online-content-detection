from flask import Flask,request, flash, redirect, render_template, request
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
from werkzeug.utils import secure_filename
from text_extraction import image_to_string

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
app.config["UPLOAD_FOLDER"] = "uploads/"
mail = Mail(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

ALLOWED_EXTENSIONS  = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

@app.route('/image-detection', methods = ["GET", "POST"])
def image_detection():

    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            text = image_to_string(filename)
            prediction = detect_content(text)
            return render_template('image-detection.html', prediction=prediction)

        else:
            flash("Allowed file type is {'png', 'jpg', 'jpeg'}")
            return redirect(request.url)

    return render_template('image-detection.html')


if __name__ == "__main__":

    app.run(debug = True,host="0.0.0.0", port = 8500)







