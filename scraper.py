# Import necessary modules
from bs4 import BeautifulSoup
import requests
from validate import fake_news_det as detect


# links = [
#     "https://timesofindia.indiatimes.com/city/kolkata/cyclone-jawad-live-updates-december-6-2021/liveblog/88113151.cms",
#     "https://timesofindia.indiatimes.com/sports/cricket/new-zealand-in-india/i-cant-judge-ajinkya-rahanes-form-only-he-knows-what-he-is-going-through-virat-kohli/articleshow/88120191.cms",
#     "https://timesofindia.indiatimes.com/city/mysuru/karnataka-students-tested-positive-for-covid-19-in-narasimharajapura-touches-94/articleshow/88117720.cms",
#     "https://www.gadgetsnow.com/featured/buying-a-windows-pc-which-intel-processor-is-best-suited-for-you/articleshow/88115163.cms",
#     "https://timesofindia.indiatimes.com/spotlight/transform-your-career-with-isb-executive-educations-applied-business-analytics-programme/articleshow/88052204.cms",
#     "https://timesofindia.indiatimes.com/sports/cricket/new-zealand-in-india/2nd-test-india-demolish-new-zealand-by-372-runs-claim-series-1-0/articleshow/88116745.cms",
#     "https://timesofindia.indiatimes.com/india/to-test-vaccine-efficacy-icmr-isolating-omicron-strain/articleshow/88112063.cms"
# ]



url_text = requests.get("https://timesofindia.indiatimes.com/india/to-test-vaccine-efficacy-icmr-isolating-omicron-strain/articleshow/88112063.cms").text
soup = BeautifulSoup(url_text,'lxml')


# get all tags
tags = {tag.name for tag in soup.find_all()}
  
# class_list = []

# iterate all tags
# for tag in tags:
  
#     # find all element of tag
#     for i in soup.find_all( tag ):
  
#         # if tag has attribute of class
#         if i.has_attr( "class" ):
  
#             if len( i['class'] ) != 0:
#                 class_list.append(" ".join( i['class']))
  
# print(set(class_list))

delim = "---------------------------------------------------------------------------------------------\n\n"
content = []
class_list = []
print(tags)

for cls in set(class_list):

    text = soup.find_all("div", class_ = cls)

    for t in text:

        if t not in content:

            content.append(t.get_text())

content = list(set(content))

for c in content:
    print(c)
    print("*"*50)

# with open("trash.txt", "w") as f:
#     for c in content:
#         f.write(c)

# print (detect(" ".join(content)))
# print (content)"
