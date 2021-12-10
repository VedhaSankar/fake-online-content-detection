from bs4.element import ContentMetaAttributeValue
import requests
from bs4 import BeautifulSoup
import io
import PyPDF2
from PyPDF2 import PdfFileReader
import urllib
import urllib.request
from io import StringIO

new_data = '1.pdf'

pdfFileObject = open(new_data, 'rb') 
# pdfFileObject = open(data[0], 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObject) 
print(" No. Of Pages :", pdfReader.numPages) 
pageObject = pdfReader.getPage(0) 
print(pageObject.extractText()) 
pdfFileObject.close()