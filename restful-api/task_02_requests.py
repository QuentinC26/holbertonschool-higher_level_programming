#!/usr/bin/python3
import requests, json, csv
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
def fetch_and_print_posts():
    if response.status_code == 200:
        print("Status Code:", response.status_code)
        data = response.json()
        print(data['title'])
    else:
        print("Status Code:", response.status_code)
def fetch_and_save_posts():
    pass