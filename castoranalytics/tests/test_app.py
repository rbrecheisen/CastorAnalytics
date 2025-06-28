import pytest

from castoranalytics.core.loaders.studyloader import StudyLoader
from castoranalytics.core.credentials import Credentials
from tests.sources import get_sources

SOURCES = get_sources()



@pytest.fixture(scope='session')
def credentials():
    credentials = Credentials()
    with open(SOURCES['castorclientid_file'], 'r') as f:
        credentials.set_client_id(f.readline().strip())
    with open(SOURCES['castorclientsecret_file'], 'r') as f:
        credentials.set_client_secret(f.readline().strip())
    return credentials


def test_study_loader(credentials):
    loader = StudyLoader(credentials)
    studies = loader.load()
    assert len(studies) > 0
    for study in studies:
        print(study)