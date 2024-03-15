
import pytest
import pytest
import pytest_cov

from test_2 import extract_court_info, find_closest_court, get_courts


class TestLoadCourts:
    """Contains tests for loading the courts from an API"""

    def test_requests_courts(self, requests_mock, test_url):
        """Tests that one GET request is made."""
        requests_mock.get(test_url.format('E14 4PU'),
                          status_code=200, json={})
        get_courts(test_url, 'E14 4PU', "Family Court")

        assert requests_mock.called
        assert requests_mock.call_count == 1
        assert requests_mock.last_request.method == "GET"

    def test_courts_valid(self, requests_mock, test_url, test_courts_data):
        """Tests that the function returns the correct keys and output form the api"""
        requests_mock.get(test_url.format('E14 4PU'),
                          status_code=200, json=test_courts_data)
        courts = get_courts(test_url, 'E14 4PU', "Family Court")

        assert isinstance(courts, list)

        court = courts[0]

        assert "name" in court
        assert "dx_number" in court
        assert "distance" in court
        assert len(court) == 3


def test_find_closest_court_valid(test_closest_courts):
    """Tests if the function gets the closest court"""

    result = find_closest_court(test_closest_courts)
    closest_court = {'name': 'Inner London Crown Court',
                     'dx_number': '97345 Southwark 3', 'distance': 1.37}

    assert result == closest_court


def test_find_closest_court_empty():
    """Tests the function with a wrong type as input"""
    with pytest.raises(ValueError, match="Error: No courts given"):
        find_closest_court('')


def test_extract_court_info_valid(test_courts_data):
    """Tests to see if the right information is extracted"""

    courts = extract_court_info(test_courts_data, "Family Court")
    court = courts[0]

    assert len(courts) == 1
    assert "name" in court
    assert "dx_number" in court
    assert "distance" in court
    assert len(court) == 3


def test_extract_court_info_wrong_type_given(test_courts_data):
    """Tests to see if the right information is extracted"""

    courts = extract_court_info(test_courts_data, "Crown Court")

    assert len(courts) == 0
