import numpy as np 
import pandas as pd 

import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import pickle

#ignore warnings
import warnings

warnings.filterwarnings('ignore')

def save_model():

    df = pd.read_csv("news.csv")
    labels=df.label
    x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)


    #DataFlair - Initialize a TfidfVectorizer
    tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

    #DataFlair - Fit and transform train set, transform test set
    tfidf_train = tfidf_vectorizer.fit_transform(x_train) 
    tfidf_test = tfidf_vectorizer.transform(x_test)

    #DataFlair - Initialize a PassiveAggressiveClassifier
    pac = PassiveAggressiveClassifier(max_iter=50)
    pac.fit(tfidf_train,y_train)

    with open('model.pickle', 'wb') as f:
        pickle.dump(pac, f)


def load_model():

    with open('model.pickle','rb') as f:
        loaded_obj = pickle.load(f)


def predict_authentication(title, text):

    pac = load_model()

    data = {
        "title" : [title],
        "text"  : [text]    
    }

    z_test = pd.DataFrame(data)

    print (z_test)

    auth = pac.predict(z_test)

    print (auth)

    #DataFlair - Predict on the test set and calculate accuracy
    # y_pred = pac.predict(tfidf_test)
    # score = accuracy_score(y_test,y_pred)
    # print(f'Accuracy: {round(score*100,2)}%')

def startpy():

    # save_model()

    title = '''
        A Crypto Ban? The Bill Not Final, Looks At Checks And Balances: Report
    '''

    text = '''
        India is considering a proposal to treat cryptocurrencies as a financial asset while safeguarding small investors, according to people familiar with the matter.
        The discussions come as authorities race to finalize a bill the Centre wants to present to parliament in the session starting November 29. The legislation may stipulate a minimum amount for investments in digital currencies while banning their use as legal tender, the people said, asking not to be identified as no final decision has been taken.

        Policy makers left themselves some wiggle room when they posted a description of the bill on parliament's website late Tuesday, by saying the bill seeks to prohibit all private cryptocurrencies except "certain exceptions to promote the underlying technology of cryptocurrency and its uses."

        The uncertainty triggered a sell-off on Wednesday in cryptocurrencies including Shiba Inu and Dogecoin, which were at one point down more than 20% in trading on the WazirX platform, one of India's leading cryptocurrency exchanges. They were far less affected on trading platforms such as Binance or Kraken.

        A spokesman for the finance ministry couldn't be immediately reached for a comment.
    '''


    predict_authentication(title, text)

    # print(value)


if __name__== "__main__":

    startpy()