#!/usr/bin/python3

"""  Gather data from an API"""
import json
import requests


def get_todo():
    url_all_users = f"https://jsonplaceholder.typicode.com/users"
    users = requests.get(url_all_users).json()
    json_data_dic = {}
    with open(f'todo_all_employees.json', 'w') as jf:
        for user in users:
            url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                user['id'])
            respond_todo = requests.get(url).json()
            name = user['username']
            user_id = user['id']
            json_data_list = []
            for item in respond_todo:
                dic = {
                    'username': name, 'task': item["title"],
                    'completed': item["completed"],
                }

                json_data_list.append(dic)
            json_data_dic[item['userId']] = json_data_list
        json.dump(json_data_dic, jf)


if __name__ == '__main__':
    get_todo()
