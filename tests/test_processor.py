from datetime import datetime
from processor import calculate_moving_average


def test_empty_input():
    result = calculate_moving_average([], 10)
    assert result == []


def test_single_event():
    events = [
        {"timestamp": datetime(2018,12,26,18,11,8), "minute": datetime(2018,12,26,18,11), "duration": 20}
    ]
    result = calculate_moving_average(events, 10)
    assert result[0]["average_delivery_time"] == 0   # first row always 0
    assert result[1]["average_delivery_time"] == 20  # event appears in next row


def test_window_eviction():
    events = [
        {"timestamp": datetime(2018,12,26,18,0,0), "minute": datetime(2018,12,26,18,0), "duration": 100},
        {"timestamp": datetime(2018,12,26,18,15,0), "minute": datetime(2018,12,26,18,15), "duration": 10},
    ]
    result = calculate_moving_average(events, 10)
    result_map = {r["date"]: r["average_delivery_time"] for r in result}

    assert result_map["2018-12-26 18:01:00"] == 100  # first event in window
    assert result_map["2018-12-26 18:15:00"] == 0    # first evicted, second not yet admitted
    assert result_map["2018-12-26 18:16:00"] == 10   # second event now admitted


def test_challenge_example():
    events = [
        {"timestamp": datetime(2018,12,26,18,11,8,509654), "minute": datetime(2018,12,26,18,11), "duration": 20},
        {"timestamp": datetime(2018,12,26,18,15,19,903159), "minute": datetime(2018,12,26,18,15), "duration": 31},
        {"timestamp": datetime(2018,12,26,18,23,19,903159), "minute": datetime(2018,12,26,18,23), "duration": 54},
    ]
    result = calculate_moving_average(events, 10)
    result_map = {r["date"]: r["average_delivery_time"] for r in result}

    assert result_map["2018-12-26 18:11:00"] == 0
    assert result_map["2018-12-26 18:12:00"] == 20
    assert result_map["2018-12-26 18:16:00"] == 25.5
    assert result_map["2018-12-26 18:22:00"] == 31
    assert result_map["2018-12-26 18:24:00"] == 42.5