# Import necessary modules
from bs4 import BeautifulSoup
import requests



links = [
    "https://timesofindia.indiatimes.com/city/kolkata/cyclone-jawad-live-updates-december-6-2021/liveblog/88113151.cms",
    "https://timesofindia.indiatimes.com/sports/cricket/new-zealand-in-india/i-cant-judge-ajinkya-rahanes-form-only-he-knows-what-he-is-going-through-virat-kohli/articleshow/88120191.cms",
    "https://timesofindia.indiatimes.com/city/mysuru/karnataka-students-tested-positive-for-covid-19-in-narasimharajapura-touches-94/articleshow/88117720.cms",
    "https://www.gadgetsnow.com/featured/buying-a-windows-pc-which-intel-processor-is-best-suited-for-you/articleshow/88115163.cms",
    "https://timesofindia.indiatimes.com/spotlight/transform-your-career-with-isb-executive-educations-applied-business-analytics-programme/articleshow/88052204.cms",
    "https://timesofindia.indiatimes.com/sports/cricket/new-zealand-in-india/2nd-test-india-demolish-new-zealand-by-372-runs-claim-series-1-0/articleshow/88116745.cms",
    "https://timesofindia.indiatimes.com/india/to-test-vaccine-efficacy-icmr-isolating-omicron-strain/articleshow/88112063.cms"
]


url_text = requests.get(LINK).text
soup = BeautifulSoup(url_text,'lxml')

# text = url_text.find_all("div", class_ = "header-main__wrapper")

for para in soup.find_all("p"):
    print(para.get_text())


# for para in url_text.find("p"):
#     print(para.get_text()[0])

# print (url_text)