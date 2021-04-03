"Handle collections of posts"

# pylint: disable=missing-class-docstring, missing-function-docstring, invalid-name

import json
import requests

def h_js():
    return {"Content-Type":"application/json"}
def h_authjs(token):
    return {"Authorization": "Token %s" % token,
            "Content-Type":"application/json"}

class Collection(object):
    def __init__(self, domain):
        self.uri = 'https://{}/api/collections'.format(domain)

    def get(self, alias):
        c = requests.get(self.uri + "/%s" % alias,
                         headers=h_js())

        if c.status_code != 200:
            return "Error in retrieveCollection(): %s" % c.json()["error_msg"]

        collection = c.json()["data"]
        return collection


    def create(self, token, alias, title):
        data = {"alias": alias,
                "title": title}

        c = requests.post(self.uri, data=json.dumps(data),
                          headers=h_authjs(token))

        if c.status_code != 201:
            return "Error in createCollection(): %s" % c.json()["error_msg"]

        collection = c.json()["data"]
        return collection

    def delete(self, token, alias):
        c = requests.delete(self.uri + "/%s" % alias,
                            headers=h_authjs(token))

        if c.status_code != 204:
            return "Error in deleteCollection(): Invalid token or collection."

        return "Collection deleted!"

    def getP(self, alias, slug):
        p = requests.get(self.uri + "/%s/posts/%s" % (alias, slug),
                         headers=h_js())

        if p.status_code != 200:
            return "Error in retrieveCPost(): %s" % p.json()["error_msg"]

        cpost = p.json()["data"]
        return cpost

    def getPs(self, alias, page=1):
        p = requests.get(self.uri + "/%s/posts" % alias,
                         params={'page': page})

        if p.status_code != 200:
            return "Error in retrieveCPosts(): %s" % p.json()["error_msg"]

        cposts = p.json()["data"]
        return cposts

    def createP(self, token, alias, body, title=None):
        data = {"body": body,
                "title": title}

        p = requests.post(self.uri + "/%s/posts" % alias, data=json.dumps(data),
                          headers=h_authjs(token))

        if p.status_code != 201:
            return "Error in createCPost(): %s" % p.json()["error_msg"]

        cpost = p.json()["data"]
        return cpost

    def claimP(self, token, alias, post_id):
        data = [{"id": post_id}]

        p = requests.post(self.uri + "/%s/collect" % alias, data=json.dumps(data),
                          headers=h_authjs(token))

        if p.status_code != 200:
            return "Error in claimCPost(): %s" % p.json()["error_msg"]

        post = p.json()["data"]
        return post

    def pin(self, token, alias, post_id, position=1):

        data = [{"id": post_id,
                 "position": position,}]

        p = requests.post(self.uri + "/%s/pin" % alias, data=json.dumps(data),
                          headers=h_authjs(token))

        if p.status_code != 200:
            return "Error in pinPost(): %s" % p.json()["error_msg"]

        post = p.json()["data"]
        return post

    def unpin(self, token, alias, post_id):
        data = [{"id": post_id}]

        p = requests.post(self.uri + "/%s/unpin" % alias, data=json.dumps(data),
                          headers=h_authjs(token))

        if p.status_code != 200:
            return "Error in unpinPost(): %s" % p.json()["error_msg"]

        post = p.json()["data"]
        return post
