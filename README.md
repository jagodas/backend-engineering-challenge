README.md
# Unbabel Challenge

## Requirements
Python 3.7+

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
pip install pytest
```

## Run
```bash
python cli.py --input_file events.json --window_size 10
```

## Input format
The input file must be newline-delimited JSON — one object per line, no array brackets:
```json
{"timestamp": "2018-12-26 18:11:08.509654", "translation_id": "1", "event_name": "translation_delivered", "duration": 20}
{"timestamp": "2018-12-26 18:15:19.903159", "translation_id": "2", "event_name": "translation_delivered", "duration": 31}
```
Events must be ordered by timestamp from oldest to newest.

## Output
One JSON object per minute from the first to the last event:
```json
{"date": "2018-12-26 18:11:00", "average_delivery_time": 0}
{"date": "2018-12-26 18:12:00", "average_delivery_time": 20}
```

## Tests
```bash
pytest
```

## Notes
The input events are ordered by timestamp, which allows the moving average to be computed using a sliding window approach.

Each event is added to the window once and removed once as the window moves forward in time. 
