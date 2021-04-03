"User class for all user-centric operations"

import json
import requests

class User(object):
    "Core user class"
    def __init__(self, domain):
        self.domain = domain
        self.uri = 'https://{}/api/me'.format(domain)

    def auth(self, user, password):
        """
        This is how you will authenticate your account and retreive an access
        token for future requests
        """
        data = {"alias": user, "pass": password}

        r = requests.post('https://{}/auth/login'.format(self.domain), data=json.dumps(data),
                          headers={"Content-Type":"application/json"})

        if r.status_code != 200:
            return "Error in login(): %s" % r.json()["error_msg"]

        user = r.json()["data"]
        return user

    def authout(self, token):
        "Perform a logout"
        r = requests.delete("https://{}/api/auth/me".format(self.domain),
                            headers={"Authorization": "Token %s" % token})

        if r.status_code != 204:
            return "Error in logout(): %s" % r.json()["error_msg"]
        return "You are logged out!"

    def getPosts(self, token):
        posts = requests.get(self.uri + "/posts",
                             headers={"Authorization":"Token %s" % token,
                                      "Content-Type":"application/json"})

        if posts.status_code != 200:
            return "Error in retrievePosts(): %s" % posts.json()["error_msg"]

        uposts = posts.json()["data"]
        return uposts

    def getCollections(self, token):
        colls = requests.get(self.uri + "/collections",
                             headers={"Authorization":"Token %s" % token,
                                      "Content-Type":"application/json"})

        if colls.status_code != 200:
            return "Error in retrieveCollections(): %s" % colls.json()["error_msg"]

        ucollections = colls.json()["data"]
        return ucollections

    def getChannels(self, token):
        chans = requests.get(self.uri + "/channels",
                             headers={"Authorization":"Token %s" % token,
                                      "Content-Type":"application/json"})

        if chans.status_code != 200:
            return "Error in retrieveChannels(): %s" % chans.json()["error_msg"]

        uchannels = chans.json()["data"]
        return uchannels
