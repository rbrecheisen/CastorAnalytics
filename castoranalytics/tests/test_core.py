import pytest

from castoranalytics.core import Core
from castoranalytics.core.api.study import Study
from castoranalytics.core.api.country import Country


@pytest.fixture(scope='session')
def client_id():
    with open('C:\\Users\\r.brecheisen\\castorclientid.txt', 'r') as f:
        return f.readline().strip()
    

@pytest.fixture(scope='session')
def client_secret():
    with open('C:\\Users\\r.brecheisen\\castorclientsecret.txt', 'r') as f:
        return f.readline().strip()
    

@pytest.fixture(scope='session')
def token_url():
    return 'https://data.castoredc.com/oauth/token'
    

@pytest.fixture(scope='session')
def api_base_url():
    return 'https://data.castoredc.com/api'


def test_get_countries(client_id, client_secret, token_url, api_base_url):
    core = Core(client_id, client_secret, token_url, api_base_url)
    assert core is not None
    countries = core.get_countries()
    assert len(countries) > 0
    assert isinstance(countries, list)
    for country in countries:
        assert isinstance(country, Country)
        assert isinstance(country.get_id(), str)
        assert isinstance(country.get_name(), str)
        assert isinstance(country.get_tld_code(), str)
        assert isinstance(country.get_two_digit_code(), str)
        assert isinstance(country.get_three_digit_code(), str)
    

def test_get_studies(client_id, client_secret, token_url, api_base_url):
    core = Core(client_id, client_secret, token_url, api_base_url)
    assert core is not None
    studies = core.get_studies()
    assert len(studies) > 0
    assert isinstance(studies, list)
    for study in studies:
        assert isinstance(study, Study)
        assert isinstance(study.get_id(), str)
        assert isinstance(study.get_name(), str)
        assert isinstance(study.get_created_on(), str)