import json
import requests

from elections.us_states import postal_abbreviations

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('address_form', __name__, url_prefix='/')

BASE_OCD_STR = 'ocd-division/country:us'
BASE_TURBOVOTE_API_URL = 'https://api.turbovote.org/elections/upcoming'


class Address(object):
    """
    Simple data class to wrap common address format
    """

    def __init__(self, street_1=None, street_2=None, city=None, state=None, zip=None):
        self.street_1 = street_1
        self.street_2 = street_2
        self.city = city
        self.state = state
        self.zip = zip

    def to_digest(self):
        """
        Helper function to flatten the data object into a dict of vars to be sent to the frontend

        :return: Dict
        """
        return {
            'street_1': self.street_1,
            'street_2': self.street_2,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
        }


@bp.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        address = Address(street_1=request.form['street'],
                          street_2=request.form['street-2'],
                          city=request.form['city'],
                          state=request.form['state'],
                          zip=request.form['zip'])
        # To make this more robust, the API response could be parsed and processed on the backend to ensure
        # it fits the expected pattern and gracefully error if not
        results = find_elections(address)
        return render_template('election_results.html', results=results, address=address.to_digest())

    return render_template('address_form.html', states=postal_abbreviations)


def find_elections(address):
    """
    Given an address, return the results of a call to the turbovote API for all OCD strings associated
    with that address.

    :param address: Address object
    :return: JSON list of results of API call
    """
    ocd_strs = generate_ocd_strs(address)

    api_url = '{}?district-divisions={}'.format(BASE_TURBOVOTE_API_URL, ','.join(ocd_strs))
    headers = {'Accept': 'application/json'}
    results = requests.get(api_url, headers=headers)
    return json.loads(results.text)


def generate_ocd_strs(address):
    """
    Given an address, this should generate all OCD strings possible. At the moment, it only
    generates the strings for the state without other info, and state and place.

    :param address: Address object
    :return: list of valid OCD strings for the address
    """
    ocd_strs = []
    if address.state:
        ocd_strs.append(format_ocd_str(address.state))
        if address.city:
            ocd_strs.append(format_ocd_str(address.state, 'place', address.city))
    else:
        # If no state is given, return a valid string that is just the country
        ocd_strs.append(format_ocd_str())

    return ocd_strs


def format_ocd_str(state=None, additional_key=None, additional_value=None):
    """
    Builder function to create an OCD string in the right format. At the moment, no input checking
    is applied, but it could be added to gracefully handle logical issues (value without key, key without state).
    If no params are given, it creates a valid string with no state.

    :param state: two letter state abbreviation, e.g. NY
    :param additional_key: key to be sent to the API, e.g. 'place'
    :param additional_value: value to be associated with the key
    :return: OCD string, e.g. ocd-division/country:us/state:ny/place:brookyln
    """
    if not state:
        return BASE_OCD_STR
    ocd_str = '{}/state:{}'.format(BASE_OCD_STR, state.lower())
    if additional_key and additional_value:
        ocd_str += '/{}:{}'.format(additional_key, _sanitize_str_for_turbovote_API_request(additional_value))
    return ocd_str


def _sanitize_str_for_turbovote_API_request(string):
    """
    Simple helper function to apply sanitization to a string before sending to the TurboVote API.
    At the moment, it lowercases the string and substitutes underscores for spaces

    :param string
    :return: string with neccessary formatting applied
    """
    if not string:
        return ''
    return string.lower().replace(' ', '_')
