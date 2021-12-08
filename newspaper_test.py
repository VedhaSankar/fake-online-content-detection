from newspaper import Article
from requests.api import delete
# import feedparser
from validate import fake_news_det as detect


def get_content(url):

    article = Article(url)

    article.download()

    article.parse()

    content = article.text

    return content


def detect_link(url):

    # url = input ("Enter url: ")

    content = get_content(url)

    pred = detect(content)

    return pred
    

def test():

    url = "https://timesofindia.indiatimes.com/business/cryptocurrency/bitcoin/proposed-bill-banning-crypto-payments-could-mean-jail-for-violations-report/articleshow/88145125.cms"

    pred = detect_link(url)

    print (pred)


if __name__=='__main__':

    test()


# NewsFeed = feedparser.parse(url)
# entry = NewsFeed.entries

# # print (entry.keys())
# print (entry)