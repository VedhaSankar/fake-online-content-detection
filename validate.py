import numpy as np 
import pandas as pd
from sklearn import svm 

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# import train
import pickle

# NLP libraries to clean the text data
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

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


def fake_news_det(news):

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


def main():

    text = '''
        WASHINGTON (Reuters) - Steve Bannon, a former top White House strategist and a former chief campaign aide to Donald Trump, has been asked to testify before the U.S. House of Representatives intelligence panel next month, Bloomberg News reported. Corey Lewandowski, Trump’s former campaign manager, was also asked to testify in early January, Bloomberg reported on Friday, citing an official familiar with the committee’s schedule.  Representatives for the committee did not immediately respond to inquiries for comment. The panel is probing alleged Russian meddling into the 2016 U.S. election. 
    '''

    fake_news_det(text)


main()