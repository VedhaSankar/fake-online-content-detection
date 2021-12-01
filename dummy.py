import numpy as np 
import pandas as pd 


import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC

# NLP libraries to clean the text data
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import nltk

# nltk.download('stopwords')

'''
Source: https://www.kaggle.com/prawn33/fake-news-detection
'''

text = '''
The number of cases of cops brutalizing and killing people of color seems to see no end. Now, we have another case that needs to be shared far and wide. An Alabama woman by the name of Angela Williams shared a graphic photo of her son, lying in a hospital bed with a beaten and fractured face, on Facebook. It needs to be shared far and wide, because this is unacceptable.It is unclear why Williams  son was in police custody or what sort of altercation resulted in his arrest, but when you see the photo you will realize that these details matter not. Cops are not supposed to beat and brutalize those in their custody. In the post you are about to see, Ms. Williams expresses her hope that the cops had their body cameras on while they were beating her son, but I think we all know that there will be some kind of convenient  malfunction  to explain away the lack of existence of dash or body camera footage of what was clearly a brutal beating. Hell, it could even be described as attempted murder. Something tells me that this young man will never be the same. Without further ado, here is what Troy, Alabama s finest decided was appropriate treatment of Angela Williams  son:No matter what the perceived crime of this young man might be, this is completely unacceptable. The cops who did this need to rot in jail for a long, long time   but what you wanna bet they get a paid vacation while the force  investigates  itself, only to have the officers returned to duty posthaste?This, folks, is why we say BLACK LIVES MATTER. No way in hell would this have happened if Angela Williams  son had been white. Please share far and wide, and stay tuned to Addicting Info for further updates.Featured image via David McNew/Stringer/Getty Images
'''


df = pd.read_csv("result.csv")

ps = PorterStemmer()

def wordopt(text):
    text = re.sub('[^a-zA-Z]', ' ',text)
    text = text.lower()
    text = text.split()
    text = [ps.stem(word) for word in text if not word in stopwords.words('english')]
    text = ' '.join(text)
    return text


X = df['text']
Y = df.Label

X, Y = df.text.fillna(' '), df.Label

#DataFlair - Split the dataset
x_train,x_test,y_train,y_test=train_test_split(X, Y, test_size=0.2, random_state=7)

data = {
        # "title" : [title],
        "text"  : text
    }

vectorization = TfidfVectorizer()


# tfidf_test=tfidf_vectorizer.transform(data)
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(data)


# print (xv_test)

svm_model = SVC(kernel='linear')
svm_model.fit(xv_train,y_train)


def fake_news_det(news):
    input_data = {"text":[news]}
    new_def_test = pd.DataFrame(input_data)
    new_def_test["text"] = new_def_test["text"].apply(wordopt) 
    new_x_test = new_def_test["text"]
    print(type(new_x_test))
    vectorized_input_data = vectorization.transform(new_x_test)
    prediction = svm_model.predict(vectorized_input_data)
    
    if prediction == 1:
        print("Real News")
    else:
        print("Fake News")


def startpy():
    fake_news_det(text)

if __name__=='__main__':
    startpy()


# PAC DOESN'T WORK -
'''
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

# print(tfidf_test)


y_pred=pac.predict(tfidf_test)

print (y_pred)
'''
'''
lab = []

for index, row in df.iterrows():

    if row['Label'] == "REAL":

        lab.append(1)

    elif row['Label'] == 'FAKE':

        lab.append(0)

# df['label'] = lab

# print (df.Label)

# df.dropna(axis=1)


# print (df.count())

'''

# merging two csv files
# df = pd.concat(
#     map(pd.read_csv, ['news.csv', 'old.csv']), ignore_index=True)
# print(df)