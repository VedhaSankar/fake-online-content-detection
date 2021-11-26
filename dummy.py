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
"Print Email http://humansarefree.com/2016/10/indias-stonehenge-7000-year-old.html A remarkable 7,000-year-old megalithic site that served as an astronomical observatory has been found in Muduma village in Telangana, India. The discovery has been hailed as one of the most significant archaeological findings in India over the last few decades.According to Times of India , the team of archeologists described it as ""the only megalithic site in India, where a depiction of a star constellation has been identified."" The ancient observatory dates to 5,000 BC and the researchers believe that it is the earliest astronomical observatory discovered in India and perhaps even in the whole of South Asia.The site consists of around 80 huge menhirs (standing stones), which are 3.5 – 4 meters tall. There are also about 2000 alignment stones, which are 30-60cm tall.According to experts, no other excavation site in India has so many menhirs concentrated in such a small area. The maximum concentration of menhirs is located in the central portion of the monument.One of the surprising details discovered at the site is a depiction of the constellation known as Ursa Major, which is formed from small cup-sized pits carved into a standing stone. The group of about 30 cup-marks were arranged in the same shape in which Ursa Major can be observed in the night sky with the naked eye. The carving depicts not only the prominent seven starts, but also the peripheral stars too. The large standing stones that form an observatory in Telangana, India ( Satya Vijayi ) Moreover, as ArcheoFeed.com reported: an ""imaginary line drawn through the top two stars point to pole star or the North Star.""Researchers believe that the site still holds many secrets. The next planned research will take a place in December led by archeologists from Korea.Numerous prehistoric observatories have already been discovered around the world, including Peru, Britain and Armenia. Thousands of years ago people were trying to understand the sky and were often using their observations to make predictions for agricultural and ceremonial purposes. The site Zorats Karer from Armenia dates back to the same period as the observatory from India. The constellation Ursa Major as it can be seen by the unaided eye ( public domain ) As Natalia Klimczak from Ancient Origins wrote :“Zorats Karer is also known as Carahunge, Karahunj, Qarahunj. It is located in an area of around 7 hectares and covers the site nearby the Dar river canyon, close to the city of Sisan. The ancient site is often called the ""A rmenian Stonehenge ,"" but the truth of what it is may be even more fascinating. Related: Stonehenge is 5,000 Years Older Than Previously Thought According to researchers, Zorats Karer could be among the world's oldest astronomical observatories, and is at least 3,500 years older than British Stonehenge. The site was rediscovered in 1984 by a team led by researcher Onik Khnkikyan. After a few months of work, Khnkikyan concluded that the site of Zorats Karer must have been an observatory. Moreover, with time, Armenian archeologists, astronomers and astrophysicists found that there were at least two other ancient sites important for prehistoric astronomy in the vicinity: Angeghakot and Metzamor. A general view of the Karahunj site near Sisian, Southern Armenia. ( CC BY-SA 4.0 ) In 1994, Zorats Karer was extensively analyzed by Professor Paris Herouni, a member of the Armenian National Academy of Science and President of the Radio Physics Research Institute in Yerevan. His expeditions revealed a great deal of fascinating information about the site. First of all, his team counted 223 stones, of which 84 were found to have holes.They measured the longitude, latitude and the magnetic deviation of the site. The researchers also created a topographical map of the monumental megalithic construction, which became the basis of further work. Finally, the main treasure of the site was unearthed – a collection of many impressive and unique astronomical objects. The researchers realized that several stones were used to make observations of the sun, moon and stars. They were located according to knowledge about the rising, culmination moments, and setting of the sun, moon and specific stars. The stones are basalt, somewhat protected by moss but smoothed by the rain and wind and full of holes and erosion. Many of the stones were damaged over time.In ancient times, the stones were shaped and arranged in what are known as the north and south arms, the central circle, the north-eastern alley, the separate standing system of circles and the chord. The stones are between 0.5 and 3 meters tall and weigh up to 10 tons. Some of them are related to burial cists."" By Natalia Klimzcak, Ancient Origins / Cover image: Main: The Ursa Major constellation (Fotlia). Inset: The megalithic site in Telangana, India ( Bangalore Mirror ) This article was originally published on Ancient Origins and has been republished with permission. Dear Friends, HumansAreFree is and will always be free to access and use. If you appreciate my work, please help me continue. 
Stay updated via Email Newsletter: Related"

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


# PAC DOESN'T WORK FFS
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