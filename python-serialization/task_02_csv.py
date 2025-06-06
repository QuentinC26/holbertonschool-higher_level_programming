#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    with open(filename, 'r', encoding='UTF-8') as csv_file:
        read_data = list(csv.DictReader(csv_file))

    with open(filename, 'w', encoding='UTF-8') as json_file:
        json.dump(read_data, json_file)
