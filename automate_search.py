from selenium import webdriver
  
# Taking input from user
search_string = input("Input the URL or string you want to search for:")
  
# This is done to structure the string 
# into search url.(This can be ignored)
search_string = search_string.replace(' ', '+') 
  
# Assigning the browser variable with chromedriver of Chrome.
# Any other browser and its respective webdriver 
# like geckodriver for Mozilla Firefox can be used
chrome_driver=r"C:\Users\Rahaarum\Desktop\driver\chromedriver"
browser = webdriver.Chrome(chrome_driver)
  
for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" +search_string + "&start=" + str(i))