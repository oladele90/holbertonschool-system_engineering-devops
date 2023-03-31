#!/usr/bin/python3
"""api that returns user_id, name tasks and completed status"""

import csv
import requests
import sys


def api_1():
    """function that returns id user tasks and completed status"""

    user_api_url = ('https://jsonplaceholder.typicode.com/users/' +
                    sys.argv[1])
    name_response = requests.get(user_api_url)
    name_list = name_response.json()
    name = name_list.get("name")
    id = name_list.get("id")
    user_name = name_list.get("username")

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
        row = (id, user_name, comp_list[i], title_list[i])
        comp_list.append(row)
        write_list.append(row)

    with open("{}.csv".format(id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for item in write_list:
            writer.writerow(item)


if __name__ == '__main__':
    api_1()
