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
url_to_scrape = "https://www.google.com/search?q=ndtv&rlz=1C1CHBF_enIN913IN913&oq=ndtv&aqs=chrome.0.69i59j46i67i131i199i433i465j0i20i131i263i433i512j0i433i512j0i131i433i512l2j0i433i512j69i60.1565j0j7&sourceid=chrome&ie=UTF-8"

# create document
html_document = getHTMLdocument(url_to_scrape)

# create soap object
soup = BeautifulSoup(html_document, 'html.parser')


# find all the anchor tags with "href"
# attribute starting with "https://"

#for link in soup.find_all('a',attrs={'href': re.compile("^https://")}):
for link in soup.find_all('cite',attrs={'href': re.compile("^https://")}):
	# display the actual urls
	print(link.get('href'))
