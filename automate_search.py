from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

DRIVER_PATH = os.environ.get('DRIVER_PATH')   

chrome_driver = DRIVER_PATH

browser = webdriver.Chrome(executable_path=DRIVER_PATH)

search_string = input("Input the URL or string you want to search for:")
  

search_string = search_string.replace(' ', '+') 
  
    
for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" +search_string + "&start=" + str(i))

#obj="("https://www.google.com/search?q=" +search_string + "&start=" + str(0))"
#print(obj)
