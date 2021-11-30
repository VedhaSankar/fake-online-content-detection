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
""Share This Baylee Luciani (left), Screenshot of what Baylee caught on FaceTime (right) 
The closest Baylee Luciani could get to her boyfriend, who’s attending college in Austin, was through video online chat. The couple had regular “dates” this way to bridge the 200-mile distance between them. However, the endearing arrangement quickly came to an end after his FaceTime was left on and caught something that left his girlfriend horrified. 
Baylee had been discussing regular things with her boyfriend, Yale Gerstein, who was on the other side of the screen on an otherwise average evening. This video chat was not unlike all the others she had with Yale from his apartment near Austin Community College until the 19-year-old girlfriend heard some scratching sounds after FaceTime had been left on. 
According to KRON , Baylee was mid-conversation with Yale when scratches at the door caught both of their attention and he got up from his bed, where the computer was, to see who was at his door. He barely turned the handle to open in when masked men entered the room and beat Yale’s face in and slammed him down on his bed while shoving a pistol in his cheek. The intruders didn’t seem to know or care that FaceTime was still on and Baylee’s face, seen in the corner, was watching everything, terrified that she was about to see her boyfriend murdered in front of her, as she watched him fight for his life. 
Admitting that she first thought it was a joke, seconds later, she came to the horrid realization that he was being robbed and called her dad, who was at home with her in Dallas, into the room. “I was scared, because they were saying I’m going to blow your head off, I’m going to kill you,” Baylee explained along with the chilling feeling she got when the intruder finally realized the video chat was running and looked right at her in the camera. “I’m like wow… seriously watching an armed robbery happen to somebody that I care about,” she added. Screengrabs of intruder forcing Yale down on his bed while Baylee and her father watch on FaceTime in horror 
With a clear view of at least one intruder’s face, Baylee began taking screenshots of the suspect in the act as she and her dad called the police to report what was going on. She got the pictures right in time since, seconds later, the intruder decided to disconnect the computer as he and the suspects took off with thousands of dollars worth of Yale’s music equipment. Although the boyfriend’s life was spared in the traumatizing ordeal for the two of them, he said that the thieves took something from him that can’t be replaced. 
“I had just finished my first album as a solo artist,” Yale said. “That’s all lost,” since they took the recordings on the equipment, which means nothing to the thieves and everything to the victim. It’s not often that you hear of FaceTime solving crimes or potentially saving lives, which is what happened in this case. Although it was difficult to watch, Baylee, being there through technology, was an instrumental part in protecting Yale, who hopefully learned that he better take advantage of Texas’ great gun laws and arm himself with more than just a computer."
"

'''


df = pd.read_csv("news.csv")

ps = PorterStemmer()

def wordopt(text):
    text = re.sub('[^a-zA-Z]', ' ',text)
    text = text.lower()
    text = text.split()
    text = [ps.stem(word) for word in text if not word in stopwords.words('english')]
    text = ' '.join(text)
    return text


X = df['Body']
Y = df.Label

X, Y = df.Body.fillna(' '), df.Label

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
    #print(new_x_test)
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
# lab = []

# for index, row in df.iterrows():

#     if row['Label'] == "REAL":

#         lab.append(1)

#     elif row['Label'] == 'FAKE':

#         lab.append(0)

# df['label'] = lab

# print (df.Label)

# df.dropna(axis=1)


# print (df.count())

'''

# merging two csv files
# df = pd.concat(
#     map(pd.read_csv, ['news.csv', 'old.csv']), ignore_index=True)
# print(df)