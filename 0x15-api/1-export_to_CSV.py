#!/usr/bin/python3
""" a Python script that, for a given employee ID, returns information about
his/her TODO list progress in CSV format """

import csv
import requests
from sys import argv


if __name__ == "__main__":
    """ Gets info about an employee todo list """
    uname = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(argv[1])).json()['username']
    employee_data = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(argv[1])).json()

    with open('{}.csv'.format(argv[1]), mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for task in employee_data:
            completed = task['completed']
            title = task['title']
            writer.writerow([argv[1], uname, completed, title])
