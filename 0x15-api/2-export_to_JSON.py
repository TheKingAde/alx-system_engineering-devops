#!/usr/bin/python3
"""
This module provides a function to fetch and
display an employee's TODO list progress from a
REST API and export the data in JSON format.
"""
import json
import requests
import sys


def export_employee_todo_progress_to_json(employee_id):
    """
    Fetch an employee's TODO list progress from a REST API
    and export the data in JSON format.
    """
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = f"{base_url}{employee_id}"
    todos_url = f"{base_url}{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data['name']

    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        })

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)


if __name__ == "__main__":
    export_employee_todo_progress_to_json(sys.argv[1])
