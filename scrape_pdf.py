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

print(list_of_pdf)

