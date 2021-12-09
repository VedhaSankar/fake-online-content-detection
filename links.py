from bs4 import BeautifulSoup
import requests

search_term = "covid"

url_text = requests.get(f"https://news.google.com/search?q={search_term}")

soup = BeautifulSoup(url_text.text, "html.parser")

links = []

data = soup.find_all("a", {"class": "VDXfz"})
for d in data[:5]:
    links.append(f"https://news.google.com{d['href'][1:]}")

for link in links:
    print(link)
    print("*" * 50)