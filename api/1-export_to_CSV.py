#!/usr/bin/python3
"""Script to gather data from an API for a given employee ID
and export their TODO list progress to a CSV file.
"""
import csv
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

    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_info:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title"),
            ])
