#!/usr/bin/python3
import os
def generate_invitations (template, attendees):
    if not template:
        return("Template is empty, no output files generated.")
    if not attendees:
        return("No data provided, no output files generated.")
    if not isinstance(template, str):
        raise TypeError("Template must be str")
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        raise TypeError("Attendees must be list of dict")
    for index, attendee in enumerate(attendees, start=1):
        new_template = template
        for key, value in attendee.items():
            if value is None:
                value = "N/A"
            if key == "name":
                new_template = new_template.replace("{name}", value)
            if key == "event_title":
                new_template = new_template.replace("{event_title}", value)
            if key == "event_date":
                new_template = new_template.replace("{event_date}", value)
            if key == "event_location":
                new_template = new_template.replace("{event_location}", value)
        if not os.path.exists(f"output_{index}.txt"):
            with open(f'output_{index}.txt', 'w') as file:
                template_content = file.write(new_template)
    print(new_template)