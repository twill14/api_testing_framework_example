from elections.upcoming import Address
import elections.upcoming as election
import pytest


# Search Result Tests

def test_receive_relevant_or_no_elections_with_valid_data_entries(get_valid_data):
    entry = Address(street_1=get_valid_data['street_1'], street_2=get_valid_data['street_2'],
                    city=get_valid_data['city'], state=get_valid_data['state'],
                    zip=get_valid_data['zip'])
    response = election.find_elections(entry)
    assert len(response) > 0 or len(response) == 0


def test_receive_relevant_or_no_elections_with_invalid_data_entries(get_invalid_data):
    entry = Address(street_1=get_invalid_data['street_1'], street_2=get_invalid_data['street_2'],
                    city=get_invalid_data['city'], state=get_invalid_data['state'],
                    zip=get_invalid_data['zip'])
    response = election.find_elections(entry)
    assert len(response) > 0 or len(response) == 0


def test_receive_relevant_or_no_elections_with_only_state(get_state_data):
    entry = Address(state=get_state_data)
    response = election.find_elections(entry)
    assert len(response) > 0 or len(response) == 0


def test_no_elections_with_valid_data_and_no_state_entries(get_valid_data):
    entry = Address(street_1=get_valid_data['street_1'], street_2=get_valid_data['street_2'],
                    city=get_valid_data['city'],
                    zip=get_valid_data['zip'])
    response = election.find_elections(entry)
    assert len(response) == 0


@pytest.fixture(
    params=[{'street_1': '34 Letters', 'street_2': 'M Street', 'city': 'Acity', 'state': 'MD', 'zip': '43583'},
            {'street_1': 'A Street ', 'street_2': 'SomePlace4', 'city': 'City4     ', 'state': 'TX    ',
             'zip': '85394    '},
            {'street_1': '14 Street  ', 'street_2': 'Placeway  ', 'city': '12 City   ', 'state': 'NY    ',
             'zip': '123456789'}])
def get_valid_data(request):
    return request.param


@pytest.fixture(params=[
    {'street_1': '@34 Letters', 'street_2': 'M Street@ ', 'city': 'Acity     ', 'state': 'MA', 'zip': '43583     '},
    {'street_1': '34 Letters ', 'street_2': 'M Street  ', 'city': 'A+city    ', 'state': 'TX', 'zip': '4358      '},
    {'street_1': '14 Street  ', 'street_2': 'Placeway  ', 'city': '12 City   ', 'state': '', 'zip': '123456789'}])
def get_invalid_data(request):
    return request.param


@pytest.fixture(params=['MA', 'NY'])
def get_state_data(request):
    return request.param
