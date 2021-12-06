from flask import Flask,request, url_for, redirect, render_template, request
import pickle
from validate import fake_news_det as detect

app = Flask(__name__)

model = pickle.load(open('model_svm.pkl','rb'))


@app.route('/', methods = ["GET","POST"])
def home():

    if request.method == "POST":
        text = request.values.get("news")
        prediction = detect(text)
        return render_template("index.html", prediction = prediction)

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