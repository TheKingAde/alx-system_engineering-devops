#!/usr/bin/python3
"""
This module provides a function to fetch and
display an employee's TODO list progress from a
REST API and export the data in CSV format.
"""
import csv
import requests
import sys


def export_employee_todo_progress_to_csv(employee_id):
    """
    Fetch an employee's TODO list progress from a REST API
    and export the data in CSV format.
    """
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = f"{base_url}{employee_id}"
    todos_url = f"{base_url}{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data['name']

    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name,
                            task['completed'], task['title']])


if __name__ == "__main__":
    export_employee_todo_progress_to_csv(sys.argv[1])
