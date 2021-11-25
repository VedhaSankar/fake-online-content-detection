import numpy as np 
import pandas as pd 


import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC


'''
Source: https://www.kaggle.com/prawn33/fake-news-detection
'''


title = '''
    A Crypto Ban? The Bill Not Final, Looks At Checks And Balances: Report
'''

text = '''
"A recent study has concluded that second-born children are more likely to end up getting in trouble at school or having issues with the law later in life—a finding that is sure to bring much pleasure to older siblings everywhere.
 
Researchers from MIT, Northwestern and University of Florida (plus a few others) followed thousands of sets of brothers in Denmark and the state of Florida—two dramatically different cultures.
 
They found that second-born boys in both locations were more apt to run afoul of authority figures than their older peers.
 
“Despite large differences in environments across the two areas, we find remarkably consistent results: In families with two or more children, second-born boys are on the order of 20 to 40 percent more likely to be disciplined in school and enter the criminal justice system compared to first-born boys even when we compare siblings,” the authors wrote in a paper about the study.
 
So, why does birth order affect the likelihood of criminality?
 
The study authors theorize that this higher risk of delinquency could be due to the fact that second-born children do not receive the one-on-one focus and doting that their older siblings did (“Marcia, Marcia, Marcia!”). As a result, they may act out as a way to get their folks to focus on them.
 
The authors also point to the fact that parents take more time off work when they have their first child compared to when they have their second child. This means that second-borns are not only competing with their older sibling for attention, they are also competing with their parents’ careers and other responsibilities.
 
Furthermore, the study authors also say that second-borns might be more apt to act out because they are looking up to their older sibling as their first role models, whereas first-borns look to adults as their first role models.
 
In other words, the oldest child spends more developmental time around adults, which, in turn, influences them to behave more maturely.
 
A second-born, on the other hand, will be looking to a toddler or a school-age child as a role model—one who will naturally be more impulsive and egotistical.
 
It comes as no surprise that previous research has found that oldest siblings tend to be smarter than their younger sisters and brothers. The reason? Parents, naturally, spend more time alone with their first children—giving them their undivided attention.
 
Many parents in the intelligence study admitted that they were less enthusiastic about engaging in enriching activities with their second and third children. What types of enriching activities, you ask? Well, bedtime stories, crafts and playing instruments—exactly the types of things that help to increase intelligence.
 
On top of all that, some mothers admitted that they were not as strict with themselves about things like drinking and smoking during their second or third pregnancies, which could contribute to adverse outcomes for their babies.
 
You Might Also Like
Easy Method Removes Your Eyebags & Wrinkles In Minutes!
Husband Divorced His Wife After Looking Closer At This Photo
Celebrity Pokies Banned In The US. Must See Before Gone
Eight Cars That Are Hard to Depreciate
Dog's Wife Is So Skinny Now And Looks Like Kate Upton
Awkward Pictures of Hotties Who Don't Wear Underpants
We Say GoodBye To Sally Fields
Brilliant Trick Melts Belly Fat Overnight (Do This Tonight!)
1 Simple Trick Removes Eye Bags & Lip Lines in Seconds
?
These content links are provided by Content.ad. Both Content.ad and the web site upon which the links are displayed may receive compensation when readers click on these links. Some of the content you are redirected to may be sponsored content. View our privacy policy here.
To learn how you can use Content.ad to drive visitors to your content or add this service to your site, please contact us at info@content.ad.
Family-Friendly Content
 Only recommend family-friendly content
Website owners select the type of content that appears in our units. However, if you would like to ensure that Content.ad always displays family-friendly content on this device, regardless of what site you are on, check the option below. Learn More"

'''


df = pd.read_csv("news.csv")

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

X = df['Body']
Y = df.Label

X, Y = df.Body.fillna(' '), df.Label

#DataFlair - Split the dataset
x_train,x_test,y_train,y_test=train_test_split(X, Y, test_size=0.2, random_state=7)

#DataFlair - Initialize a TfidfVectorizer
# tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

# #DataFlair - Fit and transform train set, transform test set
# tfidf_train=tfidf_vectorizer.fit_transform(x_train) 


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

svm_y_pred = svm_model.predict(xv_test)

print(svm_y_pred)


# PAC DOESN'T WORK FFS
'''
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

# print(tfidf_test)


y_pred=pac.predict(tfidf_test)

print (y_pred)
'''
