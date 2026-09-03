import pytest

from flight_calculator import calculate_flight_time, flight_time_table


def test_calculate_flight_time_basic_values():
    assert calculate_flight_time(0) == 180
    assert calculate_flight_time(100) == 170
    assert calculate_flight_time(500) == 130


def test_calculate_flight_time_never_goes_below_zero():
    assert calculate_flight_time(1800) == 0
    assert calculate_flight_time(2000) == 0


def test_calculate_flight_time_rejects_negative_weight():
    with pytest.raises(ValueError, match="Weight cannot be negative."):
        calculate_flight_time(-1)


def test_flight_time_table_generates_expected_rows():
    assert flight_time_table(300, 100) == [
        (0, 180.0),
        (100, 170.0),
        (200, 160.0),
        (300, 150.0),
    ]


def test_flight_time_table_validates_arguments():
    with pytest.raises(
        ValueError,
        match="Max weight must be non-negative and step must be positive.",
    ):
        flight_time_table(-1, 100)

    with pytest.raises(
        ValueError,
        match="Max weight must be non-negative and step must be positive.",
    ):
        flight_time_table(300, 0)
