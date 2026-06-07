import json
from datetime import datetime


TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

def read_events(file_path):
    events = []

    with open(file_path, "r") as file:
        for line in file:
            data = json.loads(line)


            events.append(
                {
                    "timestamp": datetime.strptime(
                        data["timestamp"],
                        TIMESTAMP_FORMAT,
                    ),
                    "duration": data["duration"],
                }
            )

    return events