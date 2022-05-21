FROM python:3.9.5-slim-buster

RUN apt-get update

RUN pip3 install -r requirements.txt

RUN python -m nltk.downloader stopwords

RUN apt-get install tesseract-ocr

RUN apt-get install tesseract-ocr-all

RUN apt-get install imagemagick

ADD . ./app

WORKDIR /app

EXPOSE 8500

CMD [ "python","app.py" ]