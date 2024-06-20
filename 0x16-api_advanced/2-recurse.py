#!/usr/bin/python3
""" requrceve function that query reddit api"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ return list of a given reddit title"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'pKL2PTBBkJt0gXrFASOUYw'}
    params = {'after': after}
    respond = requests.get(url, headers=headers, allow_redirects=False,
                           params=params)
    if respond.status_code == 200:
        datas = respond.json().get('data').get('children')
        list_titles = []
        for post in datas:
            hot_list.append(post.get('data').get('title'))
        if respond.json().get('data').get('after'):
            return recurse(subreddit, hot_list,
                           respond.json().get('data').get('after'))
        else:
            return hot_list
    else:
        return None
