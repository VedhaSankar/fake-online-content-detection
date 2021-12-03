from flask import Flask,request, url_for, redirect, render_template
import pickle
import main as m

app = Flask(__name__)

# @vedha - enter the pickle file here
model = pickle.load(open('model_svm.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")

# ---------------- START of CONTENT section -----------------

@app.route('/predict',methods=['POST'])
def send_content():
    text = request.values.get("comment[text]")

    print (text)
    #content={"paragraph":text}  
    # prediction = model.predict(text)

    prediction = m.predict(text)

    print (prediction)

    # output='{0:.{1}f}'.format(prediction[0][1], 2)
    
    # if prediction==1:
    #     return render_template('index.html',pred='The content is AUTHENTIC with an accuracy of {}'.format(prediction))
    # else:
    #     return render_template('index.html',pred='The content is fake with an accuracy of {}'.format(prediction)) 

    return render_template("index.html", prediction = prediction)

# ------------------ END of CONTENT section ---------------

# ---------------- START of LINK here section -----------------
# @app.route('/predict',methods=['POST','GET'])
# def link_predict():
#     link= request.values.get("comment[text]")
#     #li= {"link":link}
#     prediction=model.predict_proba(link)
#     output='{0:.{1}f}'.format(prediction[0][1], 2)

#     if output==1:
#         return render_template('index.html',pred='The content is AUTHENTIC with an accuracy of {}'.format(output))
#     else:
#         return render_template('index.html',pred='The content is fake with an accuracy of {}'.format(output)) 
# ------------------ END of LINK section ---------------


if __name__ == '__main__':
    app.run(debug=True)


