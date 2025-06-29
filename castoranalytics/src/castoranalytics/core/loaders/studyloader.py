from castoranalytics.core.loaders.loader import Loader
from castoranalytics.core.castorapiclient import CastorApiClient
from castoranalytics.core.data.study import Study
from castoranalytics.core.data.studycollection import StudyCollection


class StudyLoader(Loader):
    def __init__(self, credentials):
        super(StudyLoader, self).__init__(credentials)

    def load(self):
        # Notify listeners of progress
        with CastorApiClient(self.credentials()) as client:
            studies = []
            for study in client.studies():
                study_data = Study()
                study_data.set_id(study['study_id'])
                study_data.set_name(study['name'])
                studies.append(study_data)
            study_collection = StudyCollection(studies)
            return study_collection