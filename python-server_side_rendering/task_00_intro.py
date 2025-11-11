#!/usr/bin/python

import os

def generate_invitations(template, attendees):
    # error : template empty :
    if not template:
        print(f"Template is empty, no output files generated.")
        return

    # error : attendee empty :
    if not attendees:
        print(f"No data provided, no output files generated.")
        return

    # error : template not a string:
    if not isinstance(template, str):
        print("template must be a string.")
        return
    
    # error : attendee not a list of dict:
    if not isinstance(attendees, list) or not all(isinstance(guest, dict) for guest in attendees):
        print("attendees must be a list of dicts.")
        return

    for i, attendee in enumerate(attendees, start=1):
        filename = f"output_{i}.txt"
        invit = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            invit = invit.replace(f"{{{key}}}", str(value) if value is not None else "N/A")

        try:
            with open(filename, 'x') as f:
                f.write(invit)
        except FileExistsError:
            print(f"{filename} already exists.")
        except OSError as e:
            print(f"error while writing {filename} : {e}")