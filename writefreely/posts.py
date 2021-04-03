"Implements all Post-related operations"

# pylint: disable=missing-function-docstring

import json
import requests

def h_js():
    return {"Content-Type":"application/json"}
def h_authjs(token):
    return {"Authorization": "Token %s" % token,
            "Content-Type":"application/json"}

class Post(object):
    "All Post actions"
    def __init__(self, domain):
        self.uri = 'https://{}/api/posts'.format(domain)

    def get(self, post_id):
        post_res = requests.get(self.uri + "/%s" % post_id,
                                headers=h_js())

        if post_res.status_code != 200:
            return "Error in retrievePost(): %s" % post_res.json()["error_msg"]

        post = post_res.json()["data"]
        return post

    def create(self, token, body, title):
        "New post"
        data = {"body": body,
                "title": title}

        post_res = requests.post(self.uri, data=json.dumps(data),
                                 headers=h_authjs(token))

        if post_res.status_code != 201:
            return "Error in createPost(): %s" % post_res.json()["error_msg"]

        post = post_res.json()["data"]
        return post

    def update(self, token, post_id, **kwargs):
        "Update a post"
        data = json.dumps(kwargs)

        post_res = requests.post(self.uri + "/%s" % post_id, data=data,
                                 headers=h_authjs(token))

        if post_res.status_code != 200:
            return "Error in updatePost(): %s" % post_res.json()["error_msg"]

        post = post_res.json()
        return post

    def delete(self, token, post_id):
        post_res = requests.delete(self.uri + "/%s" % post_id,
                                   headers=h_authjs(token))

        if post_res.status_code != 204:
            return "Error in deletePost(): Invalid token or post doesn't exist under your account."

        return "Post deleted!"

    def claim(self, token, post_id, ptoken):
        data = [{"id": post_id,
                 "token": ptoken}]

        post_res = requests.post(self.uri + "/claim", data=json.dumps(data),
                                 headers=h_authjs(token))

        if post_res.status_code != 200:
            return "Error in claimPost(): %s" % post_res.json()["error_msg"]

        post = post_res.json()["data"]
        return post
