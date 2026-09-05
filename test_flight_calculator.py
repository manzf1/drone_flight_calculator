import pytest
from flight_calculator import calculate_flight_time, flight_time_table

def test_calculate_flight_time_zero_payload():
    assert calculate_flight_time(0) == 180


def test_calculate_flight_time_typical_payload():
    assert calculate_flight_time(500) == 130


def test_calculate_flight_time_heavy_payload_returns_zero():
    assert calculate_flight_time(2000) == 0
    assert calculate_flight_time(2500) == 0


def test_calculate_flight_time_negative_weight():
    with pytest.raises(ValueError):
        calculate_flight_time(-10)

def test_flight_time_table_returns_expected_pairs_for_even_step():
    table = flight_time_table(10, 2)
    expected = [
        (0, 180.0),
        (2, 179.8),
        (4, 179.6),
        (6, 179.4),
        (8, 179.2),
        (10, 179.0),
    ]
    assert table == expected


def test_flight_time_table_includes_zero_and_max_when_step_matches():
    table = flight_time_table(5, 5)
    expected = [
        (0, 180.0),
        (5, 179.5),
    ]
    assert table == expected


def test_flight_time_table_clamps_negative_flight_time_values_to_zero():
    table = flight_time_table(2500, 500)
    expected = [
        (0, 180.0),
        (500, 130.0),
        (1000, 80.0),
        (1500, 30.0),
        (2000, 0.0),
        (2500, 0.0),
    ]
    assert table == expected
    assert all(flight_time >= 0 for _, flight_time in table)


def test_flight_time_table_raises_value_error_when_step_is_zero():
    with pytest.raises(ValueError):
        flight_time_table(10, 0)


def test_flight_time_table_stops_before_max_when_step_does_not_divide_evenly():
    table = flight_time_table(10, 3)
    expected = [
        (0, 180.0),
        (3, 179.7),
        (6, 179.4),
        (9, 179.1),
    ]
    assert table == expected


def test_flight_time_table_handles_zero_max_weight():
    table = flight_time_table(0, 1)
    assert table == [(0, 180.0)]

            