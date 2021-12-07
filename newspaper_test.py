from newspaper import Article
from requests.api import delete
# import feedparser
from validate import fake_news_det as detect


def detect_link(url):

    # url = input ("Enter url: ")
    article = Article(url)

    article.download()

    article.parse()

    content = article.text

    pred = detect(content)

    return pred


def test():

    url = "https://timesofindia.indiatimes.com/videos/entertainment/hindi/katrina-kaif-to-wear-a-pastel-green-lehenga-designed-by-sabyasachi-for-her-wedding-with-vicky-kaushal/videoshow/88145924.cms"

    pred = detect_link(url)

    print (pred)


if __name__=='__main__':

    test()


# NewsFeed = feedparser.parse(url)
# entry = NewsFeed.entries

# # print (entry.keys())
# print (entry)