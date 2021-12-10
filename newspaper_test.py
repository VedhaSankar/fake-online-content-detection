from newspaper import Article
from requests.api import delete
# import feedparser
from validate import fake_news_det as detect


def get_content(url):

    article = Article(url)

    try:

        article.download() 

        article.parse()

        content = article.text

    except:

        return None

    return content


def detect_link(url):

    # url = input ("Enter url: ")

    content = get_content(url)

    pred = detect(content)

    return pred
    

def test():

    url = "https://www.indiatoday.in/coronavirus-outbreak/story/delhi-covid-cases-death-positivity-rate-1886156-2021-12-09"
    pred = detect_link(url)

    # print (pred)

    # content = get_content(url)
    # print(content)


if __name__=='__main__':

    test()


# NewsFeed = feedparser.parse(url)
# entry = NewsFeed.entries

# # print (entry.keys())
# print (entry)