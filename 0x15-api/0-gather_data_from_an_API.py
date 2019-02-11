#!/usr/bin/python3
""" a Python script that, for a given employee ID, returns information about
his/her TODO list progress """

import requests
from sys import argv


if __name__ == "__main__":
    """ Gets info about an employee todo list """
    # get user name from ID
    name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()['name']
    # count total tasks assigned to user id
    total = len(requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(argv[1])).json())
    # count total tasks with completed = true, pass titles into list to print
    completed = len(requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}&completed=true"
        .format(argv[1])).json())

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total))

    for task in requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}&completed=true"
            .format(argv[1])).json():
        print("\t " + task['title'])
