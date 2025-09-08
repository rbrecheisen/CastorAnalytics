import sys
import pytest

from castoranalytics.core import Core
from castoranalytics.core.api.study import Study
from castoranalytics.core.api.studysite import StudySite
from castoranalytics.core.api.studydetails import StudyDetails
from castoranalytics.core.api.country import Country

STUDY_ID = '8DA52C41-885D-4428-BCEB-8A95DA8DB1E5'
CASTOR_CLIENT_ID_FILE = 'C:\\Users\\r.brecheisen\\castorclientid.txt'
CASTOR_CLIENT_SECRET_FILE = 'C:\\Users\\r.brecheisen\\castorclientsecret.txt'

if sys.platform.startswith('darwin'):
    CASTOR_CLIENT_ID_FILE = '/Users/ralph/castorclientid.txt'
    CASTOR_CLIENT_SECRET_FILE = '/Users/ralph/castorclientsecret.txt'


@pytest.fixture(scope='session')
def client_id():
    with open(CASTOR_CLIENT_ID_FILE, 'r') as f:
        return f.readline().strip()
    

@pytest.fixture(scope='session')
def client_secret():
    with open(CASTOR_CLIENT_SECRET_FILE, 'r') as f:
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
        assert isinstance(country.get_id(), int)
        assert isinstance(country.get_name(), str)
        assert isinstance(country.get_tld_code(), str)
        assert isinstance(country.get_two_digit_code(), str)
        assert isinstance(country.get_three_digit_code(), str)


def test_get_country_codes(client_id, client_secret, token_url, api_base_url):
    core = Core(client_id, client_secret, token_url, api_base_url)
    assert core is not None
    countries = core.get_countries()
    country_codes = core.get_country_codes()
    for country in countries:
        three_digit_code = country_codes.get_three_digit_code_for(country.get_id())
        assert three_digit_code == country.get_three_digit_code()


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


def test_get_study(client_id, client_secret, token_url, api_base_url):
    core = Core(client_id, client_secret, token_url, api_base_url)
    assert core is not None
    study = core.get_study(study_id=STUDY_ID)
    assert isinstance(study, StudyDetails)
    assert isinstance(study.get_id(), str)
    assert isinstance(study.get_name(), str)
    assert isinstance(study.get_created_on(), str)
    assert study.get_nr_sites() > 0
    assert isinstance(study.get_nr_sites(), int)
    assert study.get_nr_participants() > 0
    assert isinstance(study.get_nr_participants(), int)
    assert study.get_nr_fields() > 0
    assert isinstance(study.get_nr_fields(), int)


def test_get_study_sites(client_id, client_secret, token_url, api_base_url):
    core = Core(client_id, client_secret, token_url, api_base_url)
    assert core is not None
    study_sites = core.get_study_sites(study_id=STUDY_ID)
    assert len(study_sites) > 0
    assert isinstance(study_sites, list)
    for study_site in study_sites:
        assert isinstance(study_site, StudySite)
        assert isinstance(study_site.get_id(), str)
        assert isinstance(study_site.get_abbreviation(), str)
        assert isinstance(study_site.get_country_id(), int)
        assert isinstance(study_site.get_nr_records(), int)
        assert isinstance(study_site.get_completion_percentage(), int)