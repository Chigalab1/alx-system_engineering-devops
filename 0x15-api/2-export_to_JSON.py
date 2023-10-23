#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for k in data2:
        if k['id'] == int(argv[1]):
            u_name = k['username']
            id_no = k['id']

    row = []

    for k in data:

        new_dict = {}

        if k['userId'] == int(argv[1]):
            new_dict['username'] = u_name
            new_dict['task'] = k['title']
            new_dict['completed'] = k['completed']
            row.append(new_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
