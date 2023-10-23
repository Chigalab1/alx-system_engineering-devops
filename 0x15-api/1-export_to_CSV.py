#!/usr/bin/python3

"""
Python script that exports data in the CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for j in data2:
        if j['id'] == int(argv[1]):
            employee = j['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for j in data:

            row = []
            if j['userId'] == int(argv[1]):
                row.append(j['userId'])
                row.append(employee)
                row.append(j['completed'])
                row.append(j['title'])

                writ.writerow(row)
