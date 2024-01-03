#!/usr/bin/python3
"""  Python script that, using this REST API,
 for a given employee ID, returns information
   about his/her TODO list progress  """

import csv
import requests
import sys


def TODO_LIST(id_):
    """ GET INFORMATION ABOUT THE TODO LIST"""
    url_link = 'https://jsonplaceholder.typicode.com'
    user_response = requests.get(f'{url_link}/users/{id_}')
    data_json = user_response.json()
    employee_name = data_json.get("username")
    user_id = data_json.get("id")

    todo_list = requests.get(f'{url_link}/todos?userId={id_}')
    todo_json = todo_list.json()
    # print(todo_json)
    filename = f'{user_id}.csv'

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        
        """csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                            "TASK_TITLE"])
        """

        for task in todo_json:
            csv_writer.writerow([
                str(user_id),
                employee_name,
                str(task["completed"]),
                task["title"]
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3  0-gather_data_from_an_API.py <id>")
        sys.exit(1)

    id_ = sys.argv[1]
    TODO_LIST(id_)
