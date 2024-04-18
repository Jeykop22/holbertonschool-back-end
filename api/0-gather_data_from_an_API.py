#!/usr/bin/python3
"""
A Python script that, using the JSONPlaceholder REST API
retrieves information about a user's TODO list progress.
"""

import requests
from sys import argv


def get_todo_progress(employee_id):
    """Retrieve and print the employee's TODO list progress."""

    users_api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    get_users_api_url = requests.get(users_api_url).json()

    users_todo_api_url = \
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    get_users_todo_api_url = requests.get(users_todo_api_url).json()

    task_completed = \
        [task_check for task_check in get_users_todo_api_url
         if task_check['completed']]

    total_task_completed = len(task_completed)

    all_task_check = len(get_users_todo_api_url)

    name_employee = get_users_api_url['name']

    print(f"Employee {name_employee} is done with tasks"
          f"({total_task_completed}/{all_task_check}): ")

    for task in task_completed:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    employee_id = int(argv[1])
    get_todo_progress(employee_id)
