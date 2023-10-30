from flask import Flask, render_template, request, redirect, url_for, flash
import pickle
from dotenv import load_dotenv
import os

app = Flask(__name__)

# model = pickle.load(open('model.pkl', 'rb'))

load_dotenv()

PORT = os.environ.get('PORT')
print(PORT)


@app.route('/')
def home():

    return "Fake Online Content API"


@app.route('/detect', methods=['GET','POST'])
def detect():

    print ('here')

    return 'dude'


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
