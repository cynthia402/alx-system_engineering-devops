#!/usr/bin/python3
"""  Gather data from an API"""
import requests
import sys


def get_todo():
    id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    respond = requests.get(url)
    users_list = requests.get(user_url)

    name = users_list.json().get('name')

    job_done = 0
    all_job = 0
    for row in respond.json():
        if row.get('completed'):
            job_done += 1
        all_job += 1
    user_profile = f'Employee {name} is done with tasks({job_done}/{all_job}):'

    print(user_profile)
    for row in respond.json():
        if row.get('completed'):
            print("\t", row.get('title'))


if __name__ == '__main__':
    get_todo()
