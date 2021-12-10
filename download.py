import requests
from bs4 import BeautifulSoup
import io
import PyPDF2
from PyPDF2 import PdfFileReader
import urllib
import urllib.request
from io import StringIO

#Pdf Downloading 

# pdf_path = list_of_pdf[15]
pdf_path = "https://arxiv.org/ftp/arxiv/papers/1501/1501.07088.pdf"
def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()
 
download_file(pdf_path, "Cat")