FROM python:3.9.5-slim-buster

RUN apt-get update

RUN apt-get upgrade -y

RUN python3 -m pip install nltk

RUN python -m nltk.downloader stopwords

RUN apt-get install tesseract-ocr -y

RUN apt-get install tesseract-ocr-all -y

RUN apt-get install imagemagick -y

ADD . ./app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8500

RUN python3 train.py

CMD [ "python","app.py" ]