import argparse
from processor import read_events


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_file", required=True)
    parser.add_argument("--window_size", type=int, required=True)

    args = parser.parse_args()

    events = read_events(args.input_file)

    print(f"Loaded {len(events)} events")

if __name__ == "__main__":
    main()