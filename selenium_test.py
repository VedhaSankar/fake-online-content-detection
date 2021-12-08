from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

DRIVER_PATH = os.environ.get('DRIVER_PATH')  

driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.get("http://www.google.com")


search_string = input("Input the URL or string you want to search for:")
  

search_string = search_string.replace(' ', '+') 
  
    
for i in range(1):
    matched_elements = driver.get("https://www.google.com/search?q=" +search_string + "&start=" + str(i))


element = driver.find_element_by_link_text("News")

element.click()

get_url = driver.current_url

print(get_url)