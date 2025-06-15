#!/usr/bin/python3
import requests, json, csv
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
    pass
