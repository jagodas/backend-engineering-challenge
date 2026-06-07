import json
from datetime import datetime


TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

def parse_event(line):
    data = json.loads(line)

    timestamp = datetime.strptime(data["timestamp"], TIMESTAMP_FORMAT)

    return {
        "timestamp": timestamp,
        "minute": timestamp.replace(second=0, microsecond=0),
        "duration": data["duration"]
    }

def read_events(file_path):
    events = []


    with open(file_path, "r") as f:
        for line in f:
            events.append(parse_event(line))


    return events
