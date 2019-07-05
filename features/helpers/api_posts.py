import requests

class POSTS: 
    def __init__(self):
        self.url_posts = 'https://jsonplaceholder.typicode.com/posts'
        self.access_key = 'examplo12345678754321'

    def post(self, titlle, body):
        body = {"title":titlle, "body":body}
        headers={'Authorization': self.access_key, 'Content-Type': 'application/json'}
        response = requests.get(self.url_posts, json=body, headers=headers)
        return response