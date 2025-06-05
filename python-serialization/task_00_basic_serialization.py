#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as text_file:
        json.dump(data, text_file)


def load_and_deserialize(filename):
    with open(filename, 'r') as text_file:
        read_data = json.load(text_file)
    return read_data
