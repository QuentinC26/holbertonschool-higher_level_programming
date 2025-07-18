#!/usr/bin/python3
def generate_invitations (template, attendees):
    if not template:
        return("Template is empty, no output files generated.")
    if not attendees:
        return("No data provided, no output files generated.")
    if not isinstance(template, str):
        raise TypeError("Template must be str")
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        raise TypeError("Attendees must be list of dict")
    for key, value in attendees.items():
        if key is None:
            value == "N/A"
        elif key == "name":
            new_string = template.replace("{name}", value)
        elif key == "event_title":
            new_string = template.replace("{event_title}", value)
        elif key == "event_date":
            new_string = template.replace("{event_date}", value)
        elif key == "event_location":
            new_string = template.replace("{event_location}", value)
    print(template)
    print(attendees)
