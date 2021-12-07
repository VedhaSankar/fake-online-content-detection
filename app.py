from flask import Flask,request, url_for, redirect, render_template
import pickle
import main as m

app = Flask(__name__)

model = pickle.load(open('model_svm.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def send_content():
    text = request.values.get("comment[text]")

    print (text)

    prediction = m.predict(text)

    print (prediction)
   
    return render_template("index.html", prediction = prediction)


if __name__ == '__main__':
    app.run(debug=True)


