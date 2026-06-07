import argparse
import json
from processor import read_events, calculate_moving_average


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_file", required=True)
    parser.add_argument("--window_size", type=int, required=True)

    args = parser.parse_args()

    events = read_events(args.input_file)

    results = calculate_moving_average(
        events,
        args.window_size,
    )

    for result in results:
        print(json.dumps(result))

if __name__ == "__main__":
    main()