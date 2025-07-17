#!/usr/bin/python3
def generate_invitations (template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be str")
    if not isinstance(attendees, list(dict)):
        raise TypeError("Attendees must be list of dict")
    try:
        pass
    except ValueError:
        print("Template is empty, no output files generated.")
        exit()
    try:
        for index in attendees:
            if index == "name":
                new_string = template.replace("{name}", index)
            elif index == "event_title":
                new_string = template.replace("{event_title}", index)
            elif index == "event_date":
                new_string = template.replace("{event_date}", index)
            elif index == "event_location":
                new_string = template.replace("{event_location}", index)
            elif index == "None":
                new_value = attendees.replace("None", "N/A")
    except ValueError:
        print("No data provided, no output files generated.")
        exit()
    