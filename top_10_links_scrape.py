from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
from newspaper_test import get_content
import requests
import spacy
from validate import main

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

    print (cur_url)

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

    nlp = spacy.load("en_core_sci_lg")

    doc = nlp(content)

    print(doc.ents)


def start():

    sample_content = '''
        spaCy is an open-source software library for advanced natural language processing, 
        written in the programming languages Python and Cython. The library is published under the MIT license
        and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion.
    '''

    get_search_string(sample_content)

    # search_string = "omicon"

    # get_required_links(search_string)

    # get_content_of_link()



if __name__=='__main__':

    start()