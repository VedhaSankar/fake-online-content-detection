# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
  
  
# function to extract html document from given url
def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
      
    # response will be provided in JSON format
    return response.text
  
    
# assign required credentials
# assign URL
url_to_scrape = "https://www.google.com/search?q=toi&source=lmns&hl=en-GB&sa=X&ved=2ahUKEwjZnamS69D0AhWYoUsFHT-_ADoQ_AUoAHoECAEQAA"
  
# create document
html_document = getHTMLdocument(url_to_scrape)
  
# create soap object
soup = BeautifulSoup(html_document, 'html.parser')
  
  
# find all the anchor tags with "href" 
# attribute starting with "https://"

#print(soup.find_all('a', attrs={'href': re.compile("^https://")}))

list_ = []

for link in soup.find_all('a',attrs={'href': re.compile("^https://")}):
    # display the actual urls
    #print(link.get('href'))  
    list_.append(link.get('href'))

links_list=[]

for i in range(10):
    links_list.append(list_[i])

for link in links_list:
    print(link,"\n")
    
#print(links_list)
