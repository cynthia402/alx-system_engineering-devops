#!/usr/bin/python3
""" make get request to reddit api of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """ return no of subscribe if it is valid subreddit"""
    if subreddit:
        headers = {'User-Agent': "pKL2PTBBkJt0gXrFASOUYw"}
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        respond = requests.get(url, headers=headers, allow_redirects=False)
        sub = None
        if (respond.status_code == 200):
            return respond.json().get('data').get('subscribers')
    return 0
