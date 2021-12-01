import numpy as np 
import pandas as pd
from sklearn import svm 


from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import pickle

def wordopt(text):

    ps = PorterStemmer()


    text = re.sub('[^a-zA-Z]', ' ',text)

    text = text.lower()

    text = text.split()

    text = [ps.stem(word) for word in text if not word in stopwords.words('english')]

    text = ' '.join(text)

    return text

def load_model():

    with open('model_svm.pkl','rb') as f:

        model = pickle.load(f)

    with open('vectorizer.pkl','rb') as f:

        vectorizer = pickle.load(f)
    
    return (model, vectorizer)

def predict(news):

    svm_model, vectorizer = load_model()

    input_data = {
        "text": [news]
    }

    new_def_test = pd.DataFrame(input_data)

    new_def_test["text"] = new_def_test["text"].apply(wordopt) 

    new_x_test = new_def_test["text"]

    # print(type(new_x_test))

    vectorized_input_data = vectorizer.transform(new_x_test)

    prediction = svm_model.predict(vectorized_input_data)
    
    if prediction == 1:

        return 1

    else:

        return 0

