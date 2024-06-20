#!/usr/bin/python3
"""print top ten of hot posts for a given subreddit """


import requests


def top_ten(subreddit):
    """ print top ten hot posts"""
    if subreddit:
        headers = {
                   'User-Agent': 'pKL2PTBBkJt0gXrFASOUYw',
                  }
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        response = requests.get(url, headers=headers, allow_redirects=False,
                                params={"limit": 10},)
        if response.status_code == 200:
            try:
                data = response.json()
                posts = data['data']['children']
                for post in posts:
                    title = post['data']['title']
                    print(title)
            except (KeyError, TypeError):
                pass
        else:
            print(None)
