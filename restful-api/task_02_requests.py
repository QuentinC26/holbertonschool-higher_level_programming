#!/usr/bin/python3
import requests
response = requests.get("https://api.exemple.com/data")
def fetch_and_print_posts():
    if response.status_code == 200:
        print("Status Code:", response.status_code)
        data = response.json()
        print(data)
    else:
        print("Status Code:", response.status_code)
def fetch_and_save_posts():
    pass
