import requests
from bs4 import BeautifulSoup
import io
import PyPDF2
from PyPDF2 import PdfFileReader
import urllib
import urllib.request
from io import StringIO


def get_pdf_content(filename):

    #Pdf Reading 
    pdfFileObject = open(filename, 'rb')
    
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

    num = pdfReader.numPages
    
    print(" No. Of Pages :", num)

    content = ""

    for i in range(num):

        pageObject = pdfReader.getPage(i)

        content += pageObject.extractText()

        # print(pageObject.extractText())

    pdfFileObject.close()

    print (content)

def start():

    get_pdf_content("archive_paper.pdf")


if __name__=='__main__':

    start()