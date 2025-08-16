from castoranalytics.core.data.collection import Collection


class StudyCollection(Collection):
    def __init__(self, studies):
        self._studies_by_id = self.load_by_id(studies)
        self._studies_by_name = self.load_by_name(studies)

    def load_by_id(self, studies):
        studies_by_id = {}
        for study in studies:
            studies_by_id[study.id()] = study
        return studies_by_id
    
    def load_by_name(self, studies):
        studies_by_name = {}
        for study in studies:
            studies_by_name[study.name()] = study
        return studies_by_name
    
    def all(self):
        return self._studies_by_id.values()

    def by_id(self, id):
        if id in self._studies_by_id.keys():
            return self._studies_by_id[id]
        return None
    
    def by_name(self, name):
        if name in self._studies_by_name.keys():
            return self._studies_by_name[name]
        return None
    
    def size(self):
        return len(self.all())