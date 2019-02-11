#!/usr/bin/python3
""" a Python script that, for a given employee ID, returns information about
his/her TODO list progress in CSV format """

import json
import requests
from sys import argv


if __name__ == "__main__":
    """ Gets info about an employee todo list """
    uname = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(argv[1])).json()['username']
    employee_data = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(argv[1])).json()

    employee = []
    for task in employee_data:
        task_dict = {}
        task_dict["task"] = task["title"]
        task_dict["completed"] = task["completed"]
        task_dict["username"] = uname
        employee.append(task_dict)

    final = {argv[1]: employee}

    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(final, file)
