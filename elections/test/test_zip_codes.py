from elections.upcoming import Address
import elections.upcoming as election
import pytest


# Zip Code Tests

# A state is included in this test under the assumption that the API would require it to perform the test
def test_numeric_zip_code(get_numeric_zip_code_data):
    entry = Address(state=get_numeric_zip_code_data['state'], zip=get_numeric_zip_code_data['zip'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert True


# A state is included in this test under the assumption that the API would require it to perform the test
def test_non_numeric_zip_code(get_non_numeric_zip_code_data):
    entry = Address(state=get_non_numeric_zip_code_data['state'], zip=get_non_numeric_zip_code_data['zip'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert False

# A state is included in this test under the assumption that the API would require it to perform the test
def test_5_digit_zip_code(get_5_digit_zip_code_data):
    entry = Address(state=get_5_digit_zip_code_data['state'], zip=get_5_digit_zip_code_data['zip'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert True

# A state is included in this test under the assumption that the API would require it to perform the test
def test_9_digit_zip_code(get_9_digit_zip_code_data):
    entry = Address(state=get_9_digit_zip_code_data['state'], zip=get_9_digit_zip_code_data['zip'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert True

# A state is included in this test under the assumption that the API would require it to perform the test
def test_less_than_5_digit_zip_code(get_less_than_5_digit_zip_code_data):
    entry = Address(state=get_less_than_5_digit_zip_code_data['state'], zip=get_less_than_5_digit_zip_code_data['zip'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert False

# A state is included in this test under the assumption that the API would require it to perform the test
def test_greater_than_5_less_than_9_digit_zip_code(get_greater_than_5_less_than_9_digit_zip_code_data):
    entry = Address(state=get_greater_than_5_less_than_9_digit_zip_code_data['state'],
                    zip=get_greater_than_5_less_than_9_digit_zip_code_data['zip'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert True

# A state is included in this test under the assumption that the API would require it to perform the test
def test_greater_than_9_digit_zip_code(get_greater_than_9_digit_zip_code_data):
    entry = Address(state=get_greater_than_9_digit_zip_code_data['state'],
                    zip=get_greater_than_9_digit_zip_code_data['zip'])
    response = election.find_elections(entry)
    # There are no means with which to validate this test given the current state of the project
    assert False

@pytest.fixture(
    params=[{'state': 'TX', 'zip': '54783'}, {'state': 'TX', 'zip': '39833'}, {'state': 'TX', 'zip': '38954'},
            {'state': 'TX', 'zip': '483439234'}, {'state': 'TX', 'zip': '458930294'}])
def get_numeric_zip_code_data(request):
    return request.param


@pytest.fixture(
    params=[{'state': 'TX', 'zip': 'Letters'}, {'state': 'TX', 'zip': 'Number10'}, {'state': 'TX', 'zip': '@'},
            {'state': 'TX', 'zip': '10@'}, {'state': 'TX', 'zip': '10@Letters'}])
def get_non_numeric_zip_code_data(request):
    return request.param


@pytest.fixture(
    params=[{'state': 'TX', 'zip': '54893'}, {'state': 'TX', 'zip': '48393'}, {'state': 'TX', 'zip': '23943'},
            {'state': 'TX', 'zip': '48393'}, {'state': 'TX', 'zip': '43892'}])
def get_5_digit_zip_code_data(request):
    return request.param


@pytest.fixture(params=[{'state': 'TX', 'zip': '484939203'}, {'state': 'TX', 'zip': '483934920'},
                        {'state': 'TX', 'zip': '179534344'}, {'state': 'TX', 'zip': '059383929'},
                        {'state': 'TX', 'zip': '438020930'}])
def get_9_digit_zip_code_data(request):
    return request.param


@pytest.fixture(params=[{'state': 'TX', 'zip': '2350'}, {'state': 'TX', 'zip': '235'}, {'state': 'TX', 'zip': '23'},
                        {'state': 'TX', 'zip': '2'}])
def get_less_than_5_digit_zip_code_data(request):
    return request.param


@pytest.fixture(
    params=[{'state': 'TX', 'zip': '12345678'}, {'state': 'TX', 'zip': '1234567'}, {'state': 'TX', 'zip': '123456'}])
def get_greater_than_5_less_than_9_digit_zip_code_data(request):
    return request.param


@pytest.fixture(params=[{'state': 'TX', 'zip': '1234567890'}, {'state': 'TX', 'zip': '12345678901'},
                        {'state': 'TX', 'zip': '1234567890123'}, {'state': 'TX', 'zip': '12345678901234'}])
def get_greater_than_9_digit_zip_code_data(request):
    return request.param
