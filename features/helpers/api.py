import requests


class API:
    def __init__(self, url):
        self.url = url

    def get(self, query='', headers={}):
        response = requests.get(
            self.url + query,
            headers=headers
        )

        return response

    def post(self, body, headers={'Content-Type': 'application/json'}):
        response = requests.post(
            self.url,
            headers=headers,
            json=body
        )

        return response
