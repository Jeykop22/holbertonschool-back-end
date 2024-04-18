#!/usr/bin/python3
"""
A Python script that, using the JSONPlaceholder REST API
retrieves information about a user's TODO list progress.
"""

import json
import requests
from sys import argv


def get_todo_progress(employee_id):
    """Retrieve and print the employee's TODO list progress."""

    users_api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    get_users_api_url = requests.get(users_api_url).json()

    users_todo_api_url = \
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    get_users_todo_api_url = requests.get(users_todo_api_url).json()

    completed_tasks = []
    for task in get_users_todo_api_url:
        completed_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": get_users_api_url["username"]
        })

    output_filename = f"{employee_id}.json"
    with open(output_filename, "w") as fd:
        json.dump({employee_id: completed_tasks}, fd)


if __name__ == "__main__":
    employee_id = int(argv[1])
    get_todo_progress(employee_id)
