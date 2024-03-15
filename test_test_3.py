"""Tests for challenge 3"""

import pytest

from test_3 import sum_current_time


@pytest.mark.parametrize("input,expected", [("01:02:03", 6), ("23:59:59", 141), ("11:22:33", 66), ("00:00:00", 0), ("12:00:00", 12), ("06:30:00", 36),])
def test_sum_current_time_valid(input, expected):
    """Tests the function with a valid input"""
    result = sum_current_time(input)
    assert result == expected


def test_sum_current_time_wrong_type():
    """Tests the function with a wrong type as input"""
    with pytest.raises(Exception):
        sum_current_time(123456)


def test_sum_current_time_wrong_format():
    """Tests the function with an input with the wrong format"""
    with pytest.raises(Exception):
        sum_current_time('03.12.12')


def test_sum_current_time_wrong_numbers():
    """Tests the function with an input with impossible numbers for time"""
    with pytest.raises(Exception):
        sum_current_time('34.61.62')
