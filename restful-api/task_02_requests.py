#!/usr/bin/python3
import requests
import csv
import json
response = requests.get("https://jsonplaceholder.typicode.com/posts")


def fetch_and_print_posts():
    if response.status_code == 200:
        print("Status Code:", response.status_code)
        data = response.json()
        for index in data:
            print(index['title'])
    else:
        print("Status Code:", response.status_code)


def fetch_and_save_posts():
    if response.status_code == 200:
        with open('posts.csv', 'w', encoding="UTF-8", newline="") as file:
            data = response.json()
            fieldnames = ["id", "title", "body"]
            write_file = csv.DictWriter(file, fieldnames=fieldnames)
            write_file.writeheader()
            for index in data:
                new_dictionnary = {"id": index["id"], "title": index["title"], "body": index["body"]}
                write_file.writerow(new_dictionnary)
