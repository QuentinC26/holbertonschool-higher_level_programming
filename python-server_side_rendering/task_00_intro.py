#!/usr/bin/python3
import os
def generate_invitations (template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be str")
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        raise TypeError("Attendees must be list of dict")
    if not template:
        return("Template is empty, no output files generated.")
    if not attendees:
        return("No data provided, no output files generated.")
    for index, attendee in enumerate(attendees, start=1):
        new_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            new_template = new_template.replace(f"{{{key}}}", value)
        if not os.path.exists(f"output_{index}.txt"):
            with open(f'output_{index}.txt', 'w') as file:
                template_content = file.write(new_template)
        