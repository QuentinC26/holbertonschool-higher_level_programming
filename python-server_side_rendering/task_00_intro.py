#!/usr/bin/python3
import os
def generate_invitations (template, attendees):
    if not isinstance(template, str):
        return "Error: Template must be str"
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        return "Error : Attendees must be list of dict"
    if not template:
        return "Template is empty, no output files generated."
    if not attendees:
        return "No data provided, no output files generated."
    for index, attendee in enumerate(attendees, start=1):
        new_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            else:
                value = str(value)
            new_template = new_template.replace(f"{{{key}}}", value)
        with open(f'output_{index}.txt', 'w') as file:
            file.write(new_template)
        