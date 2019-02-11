#!/usr/bin/python3
""" a Python script that returns information about all employees'
TODO list progress in JSON format """

import json
import requests
from sys import argv


if __name__ == "__main__":
    """ Gets info about an employee todo list """
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    final = {}
    for user in users:
        userId = user["id"]

        # for each user, create employee info list
        employee_data = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(userId)).json()

        employee = []
        for task in employee_data:
            task_dict = {}
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_dict["username"] = user["username"]
            employee.append(task_dict)

        final[userId] = employee

    with open('todo_all_employees.json', 'w') as file:
        json.dump(final, file)
