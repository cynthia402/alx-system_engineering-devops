#!/usr/bin/python3

"""  Gather data from an API"""
import json
import requests
import sys


def get_todo():
    id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    name = requests.get(user_url).json().get('username')
    respond = requests.get(url).json()
    json_data = []
    with open(f'{id}.json', 'w') as jf:
        for item in respond:
            dic = {
                'task': item["title"], 'completed': item["completed"],
                'username': name
            }
            json_data.append(dic)

        json.dump({item['userId']: json_data}, jf)


if __name__ == '__main__':
    get_todo()
