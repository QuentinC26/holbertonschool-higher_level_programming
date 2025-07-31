#!/usr/bin/python3
'''
Function for read a filetext
'''
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    new_list = load_from_json_file("add_item.json")
except Exception:
    new_list = []
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        new_list.append(arg)
    save_to_json_file(new_list, "add_item.json")
