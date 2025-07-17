#!/usr/bin/python3
def generate_invitations (template, attendees):
    try:
        pass
    except:
        if not isinstance(template, str):
            TypeError("The template must be string")
            exit()
        if not isinstance(attendees, list(dict)):
            TypeError("Attendees must be a list of dict")
            exit()