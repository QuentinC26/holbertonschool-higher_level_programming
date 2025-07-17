#!/usr/bin/python3
def generate_invitations (template, attendees):
    try:
        pass
    except TypeError:
        print("The template must be string")
        exit()
    except ValueError:
        print("The template must be not empty")
    try:
        for index in attendees:
            if index == "name":
                template.replace("{name}", index)
            elif index == "event_title":
                template.replace("{event_title}", index)
            elif index == "event_date":
                template.replace("{event_date}", index)
            elif index == "event_location":
                template.replace("{event_location}", index)
            elif index == "None":
                attendees.replace("None", "N/A")
    except TypeError:
        print("Attendees must be a list of dict")
        exit()