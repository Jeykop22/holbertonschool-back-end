#!/usr/bin/python3
"""
A Python script that retrieves information about all users' TODO list progress
using the JSONPlaceholder REST API and exports the data in JSON format.
"""

import json
import requests


def get_todo_progress():
    """Retrieve and organize all users' TODO list progress."""

    # Fetch information about all users
    users_api_url = "https://jsonplaceholder.typicode.com/users"
    users_data = requests.get(users_api_url).json()
    # Dictionary to store all users' tasks
    all_employees_data = {}
    # Fetch tasks for each user and organize them in the required format
    for user in users_data:
        user_id = user["id"]
        username = user["username"]
        todos_api_url = \
            f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        user_tasks = requests.get(todos_api_url).json()

        # List to store tasks for this user
        user_task_list = []

        # Organize tasks in the required format
        for task in user_tasks:
            user_task_list.append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            })

        # Add tasks for this user to the dictionary
        all_employees_data[user_id] = user_task_list

    return all_employees_data


if __name__ == "__main__":
    # Retrieve all users' tasks
    all_tasks = get_todo_progress()

    # Write the data to JSON file
    output_filename = "todo_all_employees.json"
    with open(output_filename, "w") as fd:
        json.dump(all_tasks, fd)
