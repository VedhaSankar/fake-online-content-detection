from flask import Flask, render_template
import os
from dotenv import load_dotenv
from backend_consumer import Client

load_dotenv()

app = Flask(__name__)
client = Client()

PORT = os.environ.get('PORT')

@app.route('/')
def home():
    
    return render_template("test.html")

if __name__=='__main__':
    print (PORT)
    app.run(debug=True, host='0.0.0.0', port=PORT)