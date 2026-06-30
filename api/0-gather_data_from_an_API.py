#!/usr/bin/python3
"""Script to gather data from an API for a given employee ID
and display their TODO list progress.
"""
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
    employee_name = user_info.get("name")
    done_tasks = list(filter(lambda t: t.get("completed") is True, todo_info))
    number_of_done_tasks = len(done_tasks)
    total_tasks = len(todo_info)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
