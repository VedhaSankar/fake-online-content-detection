import requests
from bs4 import BeautifulSoup
import re
import json

# Fetching the HTML
URL = 'https://www.blueclaw.co.uk'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')


# Extracting the important tags

class SeoAudit:
    def __init__(self, url):
        '''
        If the url isn't provided with a scheme, prepend with `https://`
        '''
        self.url = requests.utils.prepend_scheme_if_needed(url, 'https')
        self.domain = requests.utils.urlparse(self.url).netloc
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.text, 'html.parser')
    def get_title(self):
        '''
        Title comes still wrapped in <title> tags.
        '''
        title_tag = self.soup.title
        if title_tag is None:
            return title_tag
        '''
        Using `get_text` and `strip` to remove the <title> tag and any
        leading or trailing whitespace.
        '''
        return title_tag.get_text().strip()

    def get_seo_data(self):
        return {
            'title': self.get_title(),
            # 'metaDescription': self.get_meta_description(),
            # 'h1': self.get_first_h1(),
            # 'internalLinks': self.find_links('internal'),
            # 'internalLinksCount': len(self.find_links('internal')),
            # 'externalLinks': self.find_links('external'),
            # 'externalLinksCount': len(self.find_links('external')),
        }
    
page = SeoAudit('https://www.blueclaw.co.uk')
# print(page.get_title())
out_obj = page.get_seo_data()
with open('seoData.json', 'w') as f:
    json.dump(out_obj, f, indent=2)
