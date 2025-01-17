"For reading other people's posts"

# pylint: disable=missing-class-docstring, missing-function-docstring, invalid-name

import requests

class Reader(object):
    def __init__(self, domain):
        self.uri = 'https://{}/read/api/posts'.format(domain)

    def get(self, skip=0):

        params = {"skip": skip}

        p = requests.get(self.uri, params=params)

        if p.status_code != 200:
            return "Error in rwa(): %s" % p.json()["error_msg"]

        posts = p.json()["data"]
        return posts
