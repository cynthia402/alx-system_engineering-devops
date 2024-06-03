#!/usr/bin/python3
"""  Gather data from an API"""
import csv
import requests
import sys


def get_todo():
    id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    respond = requests.get(url).json()
    name = requests.get(user_url).json().get('username')

    save_to = f'{id}.csv'
    with open(save_to, 'w') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for item in respond:
            writer.writerow(
                [
                    item.get("userId"), name,
                    item.get("completed"), item.get("title")
                ])


if __name__ == '__main__':
    get_todo()
