#!/usr/bin/python3
"""Script to gather data from an API for a given employee ID
and export their TODO list progress to a JSON file.
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )
    user_info = requests.get(url).json()
    todo_info = requests.get(todo_url).json()
    username = user_info.get("username")

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        for task in todo_info
    ]

    json_filename = "{}.json".format(employee_id)
    with open(json_filename, "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)
