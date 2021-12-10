import requests
from bs4 import BeautifulSoup
import io
import PyPDF2
from PyPDF2 import PdfFileReader
import urllib
import urllib.request
from io import StringIO

#Pdf Reading 
pdfFileObject = open(r"Test.pdf", 'rb')
 
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

num = pdfReader.numPages
 
print(" No. Of Pages :", num)

for i in range(num):

    pageObject = pdfReader.getPage(i)

    print(pageObject.extractText())

pdfFileObject.close()