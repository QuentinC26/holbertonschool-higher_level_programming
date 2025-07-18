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
    for index in attendees:
        for key, value in index.items():
            if value is None:
                value == "N/A"
            elif key == "name":
                new_string_01 = template.replace("{name}", value)
            elif key == "event_title":
                new_string_02 = template.replace("{event_title}", value)
            elif key == "event_date":
                new_string_03 = template.replace("{event_date}", value)
            elif key == "event_location":
                new_string_04 = template.replace("{event_location}", value)
    print(template)
    print(attendees)
