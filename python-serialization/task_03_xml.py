#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import json

def serialize_to_xml(dictionary, filename):
    root_element = ET.Element("data")
    for key, values in dictionary.items():
        child_element = ET.SubElement(root_element, key)
        child_element.text = str(values)
    with open(filename, 'wb') as text_file:
        ET.ElementTree(root_element).write(text_file, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    new_dictionary = ET.parse(filename)
    root_element = new_dictionary.getroot()
    result_dict = {}
    for child in root_element:
        result_dict[child.tag] = child.text
    return result_dict