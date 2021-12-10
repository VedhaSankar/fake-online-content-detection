import requests
from bs4 import BeautifulSoup
import io
import PyPDF2
from PyPDF2 import PdfFileReader
import urllib
import urllib.request
from io import StringIO

from download import download_file
from read import get_pdf_content

#Pdf Scraping

url = "https://dailyepaper.in/times-of-india-epaper-pdf-download-2021/"


def get_pdf_links():

    read = requests.get(url)

    html_content = read.content

    soup = BeautifulSoup(html_content, "html.parser")
    
    list_of_pdf = []

    p = soup.find_all('a')

    for link in (p):

        pdf_link = (link.get('href')[:-5]) + ".pdf"

        # print(pdf_link)

        list_of_pdf.append(pdf_link)

    return list_of_pdf


def start():

    list_of_pdf = get_pdf_links()

    print (list_of_pdf)

    for idx, link in enumerate(list_of_pdf):

        try: 

            link = list_of_pdf[idx]

            file_name = "news_art_1"

            download_file(link, file_name)

            get_pdf_content(file_name)

            break
                    

        except:

            print("Exception has occured")

            pass

        # for link in list_of_pdf:

        #     download_file()
            



if __name__=='__main__':

    start()


