#!/usr/bin/python3
"""api that returns user_id, name tasks and completed status to json file"""

import json
import requests
import sys


def api_1():
    """function that returns id user tasks and completed status to json file"""

    user_api_url = ('https://jsonplaceholder.typicode.com/users/' +
                    sys.argv[1])
    name_response = requests.get(user_api_url)
    all_users = name_response.json()
    username = all_users.get("username")
    id = all_users.get("id")
    todo_api_url = ('https://jsonplaceholder.typicode.com/users/' +
                    sys.argv[1] + '/todos')
    todo_response = requests.get(todo_api_url)
    todo_list = todo_response.json()
    title_list = []
    comp_list = []
    completed = 0
    total = 0
    for obj in todo_list:
        for key, value in obj.items():
            titles = obj.get("title")
            title_list.append(titles)
            comp = obj.get("completed")
            comp_list.append(comp)
            completed += 1
            break
        total += 1
    i = 0
    write_list = []
    for i in range(total):
        row = {"username": username, "task": title_list[i], "completed":
               comp_list[i]}
        write_list.append(row)
    new_dict = {id: write_list}
    with open("{}.json".format(id), "w") as f:
        json.dump(new_dict, f)


if __name__ == '__main__':
    api_1()
