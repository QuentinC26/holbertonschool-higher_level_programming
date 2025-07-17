#!/usr/bin/python3
def generate_invitations (template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be str")
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        raise TypeError("Attendees must be list of dict")
    if not template:
        raise ValueError("Template is empty, no output files generated.")
        exit()
    if not attendees:
        raise ValueError("No data provided, no output files generated.")
        exit()
    for index in attendees:
        if index == "name":
            new_string = template.replace("{name}", index["name"])
        elif index == "event_title":
            new_string = template.replace("{event_title}", index["event_title"])
        elif index == "event_date":
            new_string = template.replace("{event_date}", index["event_date"])
        elif index == "event_location":
            new_string = template.replace("{event_location}", index["event_location"])
        elif index == None:
            new_value = index.replace(None, "N/A")
