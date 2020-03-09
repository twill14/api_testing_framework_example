from elections.upcoming import Address
import elections.upcoming as election
import pytest


# Street and City Tests

# A state is included in this test under the assumption that the API would require it to perform the test
def test_street_street2_city_with_alpha_numeric_entries(get_alpha_numeric_data):
    entry = Address(street_1=get_alpha_numeric_data['street_1'], street_2=get_alpha_numeric_data['street_2'],
                    city=get_alpha_numeric_data['city'], state=get_alpha_numeric_data['state'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert True


# A state is included in this test under the assumption that the API would require it to perform the test
def test_street_street2_city_with_non_alpha_numeric_entries(get_non_alpha_numeric_data):
    entry = Address(street_1=get_non_alpha_numeric_data['street_1'], street_2=get_non_alpha_numeric_data['street_2'],
                    city=get_non_alpha_numeric_data['city'], state=get_non_alpha_numeric_data['state'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert False


# A state is included in this test under the assumption that the API would require it to perform the test
def test_street_street2_with_alpha_numeric_city_with_non_alpha_numeric_entries(
        get_alphanum_streets_non_alphanum_city_data):
    entry = Address(street_1=get_alphanum_streets_non_alphanum_city_data['street_1'],
                    street_2=get_alphanum_streets_non_alphanum_city_data['street_2'],
                    city=get_alphanum_streets_non_alphanum_city_data['city'],
                    state=get_alphanum_streets_non_alphanum_city_data['state'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert False


# A state is included in this test under the assumption that the API would require it to perform the test
def test_street_street2_with_non_alpha_numeric_city_with_alpha_numeric_entries(
        get_nonalphanum_streets_alphanum_city_data):
    entry = Address(street_1=get_nonalphanum_streets_alphanum_city_data['street_1'],
                    street_2=get_nonalphanum_streets_alphanum_city_data['street_2'],
                    city=get_nonalphanum_streets_alphanum_city_data['city'],
                    state=get_nonalphanum_streets_alphanum_city_data['state'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert False


@pytest.fixture(params=[{'street_1': '1Letters', 'street_2': '1Letters', 'city': '1Letters', 'state': 'TX'},
                        {'street_1': 'Letters', 'street_2': 'Letters', 'city': 'Letters', 'state': 'TX'},
                        {'street_1': '1', 'street_2': '1', 'city': '1', 'state': 'TX'}])
def get_alpha_numeric_data(request):
    return request.param


@pytest.fixture(params=[{'street_1': '@', 'street_2': '@', 'city': '@', 'state': 'TX'},
                        {'street_1': '1Letters@', 'street_2': '1Letters@', 'city': '1Letters@', 'state': 'TX'}])
def get_non_alpha_numeric_data(request):
    return request.param


@pytest.fixture(params=[{'street_1': '1', 'street_2': '1', 'city': '@', 'state': 'TX'},
                        {'street_1': 'Letters', 'street_2': 'Letters', 'city': '@', 'state': 'TX'},
                        {'street_1': '1Letters', 'street_2': '1Letters', 'city': '1Letters@', 'state': 'TX'}])
def get_alphanum_streets_non_alphanum_city_data(request):
    return request.param


@pytest.fixture(params=[{'street_1': '@', 'street_2': '@', 'city': '1', 'state': 'TX'},
                        {'street_1': 'Letters@', 'street_2': 'Letters@', 'city': 'Letters', 'state': 'TX'},
                        {'street_1': '1@', 'street_2': '1@', 'city': '1Letters', 'state': 'TX'}])
def get_nonalphanum_streets_alphanum_city_data(request):
    return request.param
