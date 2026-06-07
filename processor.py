import json
from datetime import datetime, timedelta
from collections import deque


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

def calculate_moving_average(events, window_size):
    if not events:
        return []

    window = deque()
    window_sum = 0
    results = []

    current_minute = events[0]["minute"]
    end_minute = events[-1]["minute"]
    event_index = 0

    while current_minute <= end_minute + timedelta(minutes=1):
        # Admit events whose minute is strictly before current_minute
        while event_index < len(events) and events[event_index]["minute"] < current_minute:
            window.append(events[event_index])
            window_sum += events[event_index]["duration"]
            event_index += 1

        # Evict events outside the window
        left_bound = current_minute - timedelta(minutes=window_size)
        while window and window[0]["minute"] < left_bound:
            window_sum -= window.popleft()["duration"]

        average = window_sum / len(window) if window else 0

        results.append({
            "date": current_minute.strftime("%Y-%m-%d %H:%M:%S"),
            "average_delivery_time": average,
        })

        current_minute += timedelta(minutes=1)

    return results
