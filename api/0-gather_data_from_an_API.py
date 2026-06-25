#!/usr/bin/python3
"""Script that gathers data from an API and returns TODO list progress."""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display employee TODO list progress."""
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
