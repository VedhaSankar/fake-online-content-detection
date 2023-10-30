import requests
import os

API_BASE = os.environ.get('API_BASE')

class Client(object):

    def __init__(self):

        self.api_base = API_BASE
        # self.api_key  = os.getenv("API_KEY")
        

    def process_get(self, url):

        final_url = self.api_base + url

        resp = requests.get(final_url)
        
        return resp

    def process_post(self, url, data):

        final_url = self.api_base + url

        print(final_url)

        resp = requests.post(final_url, json = data)
       
        return resp