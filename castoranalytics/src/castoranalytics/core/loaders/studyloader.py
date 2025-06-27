from castoranalytics.core.loaders.loader import Loader
from castoranalytics.core.castorapiclient import CastorApiClient
from castoranalytics.core.credentials import Credentials


class StudyLoader(Loader):
    def load(self):
        credentials = Credentials()
        with CastorApiClient(credentials.client_id(), credentials.client_secret()) as client:
            pass