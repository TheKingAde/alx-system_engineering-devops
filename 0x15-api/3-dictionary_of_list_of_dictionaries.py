#!/usr/bin/python3
"""
This module provides a function to fetch and
display all employees' TODO list progress from a
REST API and export the data in JSON format.
"""
import json
import requests


def export_all_employees_todo_progress_to_json():
    """
    Fetch all employees' TODO list progress from a REST API
    and export the data in JSON format.
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users_data = users_response.json()
    todos_data = todos_response.json()

    user_tasks = {}
    for user in users_data:
        user_tasks[user['id']] = [{
            "username": user['username'],
            "task": task['title'],
            "completed": task['completed']
        } for task in todos_data if task['userId'] == user['id']]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_tasks, jsonfile)


if __name__ == "__main__":
    export_all_employees_todo_progress_to_json()
