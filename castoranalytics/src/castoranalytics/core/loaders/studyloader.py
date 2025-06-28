from castoranalytics.core.loaders.loader import Loader
from castoranalytics.core.castorapiclient import CastorApiClient


class StudyLoader(Loader):
    def __init__(self, credentials):
        super(StudyLoader, self).__init__(credentials)

    def load(self):
        # Notify listeners of progress
        with CastorApiClient(self.credentials()) as client:
            studies = client.get_studies()
            return studies