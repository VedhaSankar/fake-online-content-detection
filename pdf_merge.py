import requests
from bs4 import BeautifulSoup
import io
import PyPDF2
from PyPDF2 import PdfFileReader
import urllib
import urllib.request
from io import StringIO

#Pdf Scraping

url = "https://dailyepaper.in/times-of-india-epaper-pdf-download-2021/"
read = requests.get(url)
html_content = read.content
soup = BeautifulSoup(html_content, "html.parser")
 
list_of_pdf = []
p = soup.find_all('a')

for link in (p):
    pdf_link = (link.get('href')[:-5]) + ".pdf"
    print(pdf_link)
    list_of_pdf.append(pdf_link)

# print(list_of_pdf)

#Pdf Downloading 

# pdf_path = list_of_pdf[15]
pdf_path = "https://arxiv.org/ftp/arxiv/papers/1501/1501.07088.pdf"
def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()
 
download_file(pdf_path, "News_content")

#Pdf Reading 
pdfFileObject = open(r"News_content.pdf", 'rb')
 
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

num = pdfReader.numPages
 
# print(" No. Of Pages :", num)


news=""

for i in range(num):

    pageObject = pdfReader.getPage(i)

    news+=pageObject.extractText()

print(news)

pdfFileObject.close()