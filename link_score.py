
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
from newspaper_test import detect_link, get_content
import requests
import spacy
from similarity import check_similarity


# NLP libraries to clean the text data
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

import yake


def get_google_soup(search_string):  
    url_text = requests.get(f"https://news.google.com/search?q={search_string}")

    soup = BeautifulSoup(url_text.text, "html.parser")

    return soup

def get_required_links(search_string):

    soup = get_google_soup(search_string)

    main_div = soup.find("div", {"class": "lBwEZb BL5WZb xP6mwf"})

    all_links =  main_div.find_all('a')

    links = []

    # print (all_links)

    try:
        for idx, a_link in enumerate(all_links):
            try:

                if idx == 30:

                    a_link = a_link.get('href') 

                    a_link = a_link.split("./")[1]

                    link = "https://news.google.com/" + a_link

                    # print (link)

                    links.append(link)
                    
                    idx = idx + 1

            except:
                pass

                # break        



            # if a_link.startswith("/url?q="):

            #     link = a_link.split("/url?q=")[1]

            #     links.append(link)

            # if len(links) == 3:

            #     break

    except:
        pass

    # print(links)

    return links

    # lBwEZb BL5WZb xP6mwf

def get_content_of_link(search_string):

    links = get_required_links(search_string)

    content_list = []
    pred_list = []

    # print(links)

    for link in links:

        try:

            judge = detect_link(link)

            pred_list.append(judge)

        except:

            pass

    return (pred_list)
    
    # print(content_list)

def get_keyword_list(text):

    # text = """ The couple took their seven pheras on Thursday afternoon, a source told ANI. The wedding, being held at Six Senses, Fort Barwara in Sawai Madhopur, Rajasthan, has been something of a state secret with guests subjected to a no-phone and no-photos rule. No inside pictures or footage is available; however, it is believed that a mehendi ceremony took place on Tuesday as well as a traditional Punjabi 'ladies sangeet' organised by Vicky's mom Veena Kaushal. A haldi ceremony was held on Wednesday followed by a poolside sangeet. The wedding today is believed to have been preceded by a sehrabandi for Vicky.
    # """
    language = "en"

    max_ngram_size = 3

    deduplication_threshold = 0.9

    numOfKeywords = 5

    custom_kw_extractor = yake.KeywordExtractor(lan = language, n = max_ngram_size, dedupLim = deduplication_threshold, top = numOfKeywords, features = None)

    keywords = custom_kw_extractor.extract_keywords(text)

    keyword_list = []

    for kw in keywords:

        key, score = kw

        keyword_list.append(key)

    return keyword_list

def finalizer(pred_list):

    count = 0

    result = 0

    for num in pred_list:

        if(num==1):

            count+=1

    if(count>=2):

        result = 1

    return result



def predict_link_score(url):

    # url = "https://www.dnaindia.com/education/report-cbse-class-10-12-board-exam-2022-term-1-cancellation-latest-updates-news-exam-centre-datesheetonline-petition-2917207"
    # url = "https://www.bbc.com/sport/football/59572726"

    content = get_content(url)

    # print(content)

    keyword_list = get_keyword_list(content)

    # print(keyword_list)

    judge_list = []
    prediction = []

    for keyword in keyword_list:

        judge_list = get_content_of_link(keyword)

        # print(judge_list)

        prediction.append(judge_list)

        # for judge in judge_list:

        #     # print(judge)

        #     judge_list.append(judge)

    # print (prediction)

    pred_list = [elem for sublist in prediction for elem in sublist]

    # print (pred_list)

    result = finalizer(pred_list)   

    return result

if __name__=='__main__':
    predict_link_score()