#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, 'r', encoding='UTF-8') as text_file:
            read_data = list(csv.DictReader(text_file))
        with open("data.json", 'w', encoding='UTF-8') as written_file:
            json.dump(read_data, written_file, indent=4)
        return True
    except Exception:
        return False
