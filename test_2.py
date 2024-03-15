# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name":"East London Family Court",
        "lat":51.5063346382936,
        "lon":-0.0261344650867725,
        "number":null,
        "cci_code":null,
        "magistrate_code":null,
        "slug":"east-london-family-court",
        "types":["Family Court"],
        "areas_of_law":[{"name":"Adoption","external_link":"https://www.gov.uk/child-adoption","display_url":null,"external_link_desc":"Information about adopting a child","display_name":null,"display_external_link":"https://www.gov.uk/child-adoption/applying-for-an-adoption-court-order"},
                        {"name":"Children","external_link":null,"display_url":null,"external_link_desc":null,"display_name":"Childcare arrangements if you separate from your partner","display_external_link":"https://www.gov.uk/looking-after-children-divorce"},
                        {"name":"Divorce","external_link":"https://www.gov.uk/divorce","display_url":null,"external_link_desc":"Information about getting a divorce","display_name":null,"display_external_link":null},
                        {"name":"Domestic violence","external_link":null,"display_url":null,"external_link_desc":null,"display_name":"Domestic abuse","display_external_link":"https://www.gov.uk/injunction-domestic-violence"},
                        {"name":"FGM","external_link":"https://www.gov.uk/government/collections/female-genital-mutilation","display_url":null,"external_link_desc":null,"display_name":"Female Genital Mutilation","display_external_link":null},
                        {"name":"Forced marriage","external_link":"https://www.gov.uk/apply-forced-marriage-protection-order","display_url":null,"external_link_desc":"Information about forced marriage protection orders","display_name":null,"display_external_link":null}],
        "areas_of_law_spoe":["Children"],
        "displayed":true,
        "hide_aols":false,
        "dx_number":"316201 Docklands 3",
        "distance":0.21,
        "addresses":[{"address_lines":["East London Family Court","6th and 7th Floor, 11 Westferry Circus",
                                       "(Entrance in Columbus Courtyard)"],
                      "postcode":"E14 4HD",
                      "town":"London",
                      "type":"Visit or contact us",
                      "county":"Greater London",
                      "description":null,
                      "fields_of_law":null}]
    },
    ...
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type


import csv
import requests


def extract_court_info(courts: list[dict], type_required: str) -> list[dict]:
    """Returns a list of dicts with the useful information extracted"""
    name = 'name'
    dx_num = 'dx_number'
    distance = 'distance'
    court_type = 'types'
    new_courts = []
    for court in courts:
        if type_required in court.get(court_type):
            new_court = {}
            new_court[name] = court.get(name)
            new_court[dx_num] = court.get(dx_num)
            new_court[distance] = court.get(distance)
            new_courts.append(new_court)

    return new_courts


def get_people(file_path: str) -> list[dict]:
    """Return a list of dicts of data extracted from a csv file."""
    people = []
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = csv.DictReader(file)
        people += list(lines)
    return people


def get_courts(url: str, postcode: str, type_required: str) -> list[dict]:
    """Return a list of dictionaries of the closest courts with the data needed"""

    url = url.format(postcode)
    response = requests.get(url, timeout=10)
    if response.status_code == 404:
        raise Exception("Unable to locate postcode.",
                        response.status_code)
    if response.status_code != 200:
        raise Exception("Unable to connect to server.", response.status_code)

    courts = response.json()

    return extract_court_info(courts, type_required)


def find_closest_court(courts: list[dict]) -> dict:
    """Returns the court dictionary that is closest"""
    distance = "distance"
    closest_distance = float('inf')
    closest_court = {}

    if not courts:
        raise ValueError("Error: No courts given")

    for court in courts:
        court_distance = court.get(distance)
        if court_distance < closest_distance:
            closest_distance = court_distance
            closest_court = court

    return closest_court


def people_with_closest_court(people: list[dict]) -> dict:
    """Return a list of dictionaryies with people and their closest court with a few key details"""

    url = 'https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={}'
    people_with_courts = []
    person_name = 'person_name'
    court_type = 'looking_for_court_type'
    postcode = 'home_postcode'

    for person in people:
        person_and_court = {}
        person_and_court['name'] = person.get(person_name)
        person_and_court['court_type'] = person.get(court_type)
        person_and_court['postcode'] = person.get(postcode)

        courts = get_courts(url, person.get(postcode), person.get(court_type))
        court = find_closest_court(courts)

        person_and_court['court_name'] = court.get('name')
        person_and_court['dx_number'] = court.get('dx_number')
        person_and_court['distance'] = court.get('distance')

        people_with_courts.append(person_and_court)

    return people_with_courts


def main():
    """A function to contain the main"""
    people = get_people('people.csv')
    people_with_courts = people_with_closest_court(people)
    print(people_with_courts)


if __name__ == "__main__":
    main()
