from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
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


# python -m spacy download en_core_web_sm

load_dotenv()

DRIVER_PATH = os.environ.get('DRIVER_PATH')  

# nlp = spacy.load("en_core_sci_lg")

# Making it headless
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options = chrome_options, executable_path = DRIVER_PATH)
driver.get("http://www.google.com")


def get_google_soup(search_string):     

    search_string = search_string.replace(' ', '+') 
    
        
    for i in range(1):
        matched_elements = driver.get("https://www.google.com/search?q=" +search_string + "&start=" + str(i))


    element = driver.find_element_by_link_text("News")

    element.click()

    cur_url = driver.current_url

    # print (cur_url)

    url_text = requests.get(cur_url).text
    soup = BeautifulSoup(url_text,'lxml')

    return soup


def get_required_links(search_string):

    soup = get_google_soup(search_string)

    main_div = soup.find("div", {"id": "main"})

    all_links =  main_div.find_all('a')

    links = []

    for a_link in all_links:

        a_link = a_link['href']

        if a_link.startswith("/url?q="):

            link = a_link.split("/url?q=")[1]

            links.append(link)

        if len(links) == 3:

            break

    return links

def get_content_of_link(search_string):

    links = get_required_links(search_string)

    content_list = []

    for link in links:

        content = get_content(link)

        content_list.append(content)

    return content_list

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


def start():

    url = "https://www.ndtv.com/world-news/coronavirus-new-variant-covid-19-vaccination-on-omicron-who-shares-a-new-concern-2644260#pfrom=home-ndtv_topscroll"

    content = get_content(url)

    keyword_list = get_keyword_list(content)

    # print(keyword_list)

    content_list = []

    for keyword in keyword_list:

        cnt_list = get_content_of_link(keyword)

        for cnt in cnt_list:

            if cnt is not None:

                content_list.append(cnt)

    print (content_list)

    # check_similarity()

    # search_string = "omicon"

    # print (get_required_links(search_string))

    # get_content_of_link()



if __name__=='__main__':

    start()