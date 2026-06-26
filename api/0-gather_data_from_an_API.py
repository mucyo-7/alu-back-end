#!/usr/bin/python3
"""Gather data from an API and display employee TODO list progress."""
import requests
import sys
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    ).json()
    employee_name = user.get("name")
    done_tasks = [t for t in todos if t.get("completed")]
    total = len(todos)
    done = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done, total))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
