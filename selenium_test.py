from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests

from validate import main

load_dotenv()

DRIVER_PATH = os.environ.get('DRIVER_PATH')  

# Making it headless
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options, executable_path = DRIVER_PATH)
driver.get("http://www.google.com")


def get_google_soup(): 

    search_string = "omicon"
    

    search_string = search_string.replace(' ', '+') 
    
        
    for i in range(1):
        matched_elements = driver.get("https://www.google.com/search?q=" +search_string + "&start=" + str(i))


    element = driver.find_element_by_link_text("News")

    element.click()

    cur_url = driver.current_url

    url_text = requests.get(cur_url).text
    soup = BeautifulSoup(url_text,'lxml')

    return soup


def get_required_links():

    soup = get_google_soup()

    main_div = soup.find("div", {"id": "rso"})

    print (main_div)

    # links =  main_div.find_all('a')

    # print (links)


def start():

    get_required_links()



if __name__=='__main__':

    start()