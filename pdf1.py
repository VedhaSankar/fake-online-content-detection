from bs4.element import ContentMetaAttributeValue
import requests
from bs4 import BeautifulSoup
import io
import PyPDF2
from PyPDF2 import PdfFileReader
import urllib
import urllib.request
from io import StringIO

url = "https://www.sciencedirect.com/science/article/pii/S187704281100677X"
read = requests.get(url)
html_content = read.content
soup = BeautifulSoup(html_content, "html.parser")
 
list_of_pdf = []
l = soup.find('p')
p = l.find_all('a')

for link in (p):
    pdf_link = (link.get('href')[:-5]) + ".pdf"
    list_of_pdf.append(pdf_link)

print(list_of_pdf)

# #Saving pdf
# data = urllib.request.urlretrieve(link)
data = urllib.request.urlretrieve(data[0])


