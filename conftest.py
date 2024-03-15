
import pytest


@pytest.fixture
def test_url():
    """The url string"""
    return "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={}"


@pytest.fixture
def test_courts_data():
    """The Data being loaded by the api"""
    return [
        {
            "name": "East London Family Court",
            "lat": 51.5063346382936,
            "lon": -0.0261344650867725,
            "number": None,
            "cci_code": None,
            "magistrate_code": None,
            "slug": "east-london-family-court",
            "types": ["Family Court"],
            "areas_of_law": [{"name": "Adoption", "external_link": "https://www.gov.uk/child-adoption", "display_url": None, "external_link_desc": "Information about adopting a child", "display_name": None, "display_external_link": "https://www.gov.uk/child-adoption/applying-for-an-adoption-court-order"},
                             {"name": "Children", "external_link": None, "display_url": None, "external_link_desc": None,
                             "display_name": "Childcare arrangements if you separate from your partner", "display_external_link": "https://www.gov.uk/looking-after-children-divorce"},
                             {"name": "Divorce", "external_link": "https://www.gov.uk/divorce", "display_url": None,
                             "external_link_desc": "Information about getting a divorce", "display_name": None, "display_external_link": None},
                             {"name": "Domestic violence", "external_link": None, "display_url": None, "external_link_desc": None,
                             "display_name": "Domestic abuse", "display_external_link": "https://www.gov.uk/injunction-domestic-violence"},
                             {"name": "FGM", "external_link": "https://www.gov.uk/government/collections/female-genital-mutilation", "display_url": None,
                             "external_link_desc": None, "display_name": "Female Genital Mutilation", "display_external_link": None},
                             {"name": "Forced marriage", "external_link": "https://www.gov.uk/apply-forced-marriage-protection-order", "display_url": None, "external_link_desc": "Information about forced marriage protection orders", "display_name": None, "display_external_link": None}],
            "areas_of_law_spoe": ["Children"],
            "displayed": True,
            "hide_aols": False,
            "dx_number": "316201 Docklands 3",
            "distance": 0.21,
            "addresses": [{"address_lines": ["East London Family Court", "6th and 7th Floor, 11 Westferry Circus",
                                             "(Entrance in Columbus Courtyard)"],
                           "postcode": "E14 4HD",
                           "town": "London",
                           "type": "Visit or contact us",
                           "county": "Greater London",
                           "description": None,
                           "fields_of_law": None}]
        }
    ]


@pytest.fixture
def test_closest_courts():
    """A list of 3 courts to test which ones closest"""

    return [{'name': 'Inner London Crown Court',
             'dx_number': '97345 Southwark 3', 'distance': 1.37},
            {'name': 'Newport (South Wales) Crown Court',
            'dx_number': '99450 Caerdydd/ Cardiff 5', 'distance': 1.8},
            {'name': 'Willesden County Court and Family Court',
            'dx_number': '97560 Harlesden 2', 'distance': 4.58}
            ]
