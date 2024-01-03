#!/usr/bin/python3
"""  Python script that, using this REST API,
 for a given employee ID, returns information
   about his/her TODO list progress  """

import requests
import sys


def TODO_LIST(id_):
    """ GET INFORMATION ABOUT THE TODO LIST"""
    url_link = 'https://jsonplaceholder.typicode.com'
    user_response = requests.get(f'{url_link}/users/{id_}')
    data_json = user_response.json()
    employee_name = data_json.get("name")

    todo_list = requests.get(f'{url_link}/todos?userId={id_}')
    todo_json = todo_list.json()

    total_tasks = len(todo_json)
    completed_tasks = sum(1 for task in todo_json if task["completed"])
    print(
        f"Employee {employee_name} is done with tasks "
        f"({completed_tasks}/{total_tasks}):"
        )
    for task in todo_json:
        if task["completed"]:
            print(f"    {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3  0-gather_data_from_an_API.py <id>")
        sys.exit(1)

    id_ = sys.argv[1]
    TODO_LIST(id_)
