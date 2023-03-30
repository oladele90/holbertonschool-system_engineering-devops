#!/usr/bin/python3
"""api that returns employees and tasks completed"""
from flask import Flask
import json
import requests
import sys

if __name__ == '__main__':

    api = Flask(__name__)

    user_api_url = ('https://jsonplaceholder.typicode.com/users/' +
                    sys.argv[1])
    name_response = requests.get(user_api_url)
    name_list = name_response.json()
    name = name_list.get("name")

    todo_api_url = ('https://jsonplaceholder.typicode.com/users/' +
                    sys.argv[1] + '/todos')
    todo_response = requests.get(todo_api_url)
    todo_list = todo_response.json()
    title_list = []
    completed = 0
    total = 0
    for obj in todo_list:
        for key, value in obj.items():
            if obj.get("completed") is True:
                titles = obj.get("title")
                title_list.append(titles)
                completed += 1
                break
        total += 1
    print("Employee {} is done with tasks ({}/{}):".format(name,
                                                           completed, total))
    for item in title_list:
        print("     {}".format(item))
