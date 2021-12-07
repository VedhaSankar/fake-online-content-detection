from newspaper import Article
import feedparser
from validate import fake_news_det as detect


# url = 'https://timesofindia.indiatimes.com/india/parliament-winter-session-live-updates/liveblog/88113566.cms'
url = input ("Enter url: ")
article = Article(url)

article.download()

article.parse()

content = article.text

print (detect(content))


# NewsFeed = feedparser.parse(url)
# entry = NewsFeed.entries

# # print (entry.keys())
# print (entry)