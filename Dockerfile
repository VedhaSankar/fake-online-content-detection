FROM python:3.9.5-slim-buster

ADD . ./app

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN python -m nltk.downloader stopwords

RUN apt-get install tesseract-ocr

RUN apt-get install tesseract-ocr-all

RUN apt-get install imagemagick

EXPOSE 8500

CMD [ "python","app.py" ]