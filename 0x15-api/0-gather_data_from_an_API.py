#!/usr/bin/python3
""" a Python script that, for a given employee ID, returns information about
his/her TODO list progress """

import requests
from sys import argv


if __name__ == "__main__":
    """ Gets info about an employee todo list """
    name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()['name']
    total = len(requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(argv[1])).json())
    completed = len(requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}&completed=true"
        .format(argv[1])).json())

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total))

    for task in requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}&completed=true"
            .format(argv[1])).json():
        print("\t " + task['title'])
