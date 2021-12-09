from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
from newspaper_test import get_content
import requests
import spacy

# NLP libraries to clean the text data
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

from pyteaser import SummarizeUrl



# python -m spacy download en_core_web_sm

load_dotenv()

DRIVER_PATH = os.environ.get('DRIVER_PATH')  

# nlp = spacy.load("en_core_sci_lg")

# Making it headless
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options, executable_path = DRIVER_PATH)
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

        if len(links) == 10:

            break

    return links

def get_content_of_link(search_string):

    links = get_required_links(search_string)

    content_list = []

    for link in links:

        content = get_content(link)

        content_list.append(content)

    print (content_list)

def get_search_string(content):

    nlp = spacy.load('en_core_web_sm')

    doc = nlp(content)

    print(doc.ents)

def summarize(url):

    summaries = SummarizeUrl(url)
    print (summaries)


def start():

    sample_content = '''

    In a moment of instant Ashes infamy, Rory Burns was bowled by Mitchell Starc from the very first delivery of the series, immediately sapping English optimism in Brisbane.

With skipper Joe Root falling for nought, England were 11-3, having opted to bat on a green-tinged pitch offering assistance to the pace bowlers.

Australia's attack was relentless, led by Pat Cummins, who claimed 5-38 on his first day as captain.

Jos Buttler mounted an England counter-attack of sorts with 39, sharing a stand of 52 with Ollie Pope, who made 35.

Haseeb Hameed, with a watchful 25, and Chris Woakes, who made 21, were the only other batters to reach double figures.

The miserable batting display detracted from the decision to omit Stuart Broad, joining fellow pace bowler James Anderson on the sidelines, the first time in 15 years England have played an Ashes Test without at least one of them.
            '''

    url = 'http://www.huffingtonpost.com/2013/11/22/twitter-forward-secrecy_n_4326599.html'

    summarize(url)

    # search_string = "omicon"

    # print (get_required_links(search_string))

    # get_content_of_link()



if __name__=='__main__':

    start()