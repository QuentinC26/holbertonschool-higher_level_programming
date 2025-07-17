#!/usr/bin/python3
def generate_invitations (template, attendees):
    if not template:
        raise ValueError("Template is empty, no output files generated.")
    if not attendees:
        raise ValueError("No data provided, no output files generated.")
    if not isinstance(template, str):
        raise TypeError("Template must be str")
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        raise TypeError("Attendees must be list of dict")
    for index in attendees:
        if index == "name":
            new_string = template.replace("{name}", index["name"])
        if index == "event_title":
            new_string = template.replace("{event_title}", index["event_title"])
        if index == "event_date":
            new_string = template.replace("{event_date}", index["event_date"])
        if index == "event_location":
            new_string = template.replace("{event_location}", index["event_location"])
        if index.get("key") is None:
            index["key"] = "N/A"
    print(template)
    print(attendees)