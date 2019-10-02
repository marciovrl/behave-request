import requests


class Posts:
    def __init__(self, url):
        self.url_posts = url + "/posts"
        self.access_key = 'key123'

    def post(self, titlle, body):
        body = {"title": titlle, "body": body}
        headers = {'Authorization': self.access_key,
                   'Content-Type': 'application/json'}
        response = requests.post(self.url_posts, json=body, headers=headers)
        return response

    def get(self):
        headers = {'Authorization': self.access_key,
                   'Content-Type': 'application/json'}
        response = requests.get(self.url_posts, headers=headers)
        return response
