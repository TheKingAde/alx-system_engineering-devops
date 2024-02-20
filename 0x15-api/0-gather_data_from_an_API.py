#!/usr/bin/python3
"""This module provides a function to fetch and
display an employee's TODO list progress from a
REST API."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display an employee's TODO list
    progress from a REST API.
    """
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = f"{base_url}{employee_id}"
    todos_url = f"{base_url}{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data['name']
    total_tasks = len(todos_data)
    done_tasks = len([task for task in todos_data if task['completed']])

    print(f"Employee {employee_name} is done with tasks"
          f"({done_tasks}/{total_tasks}):")
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    get_employee_todo_progress(sys.argv[1])
