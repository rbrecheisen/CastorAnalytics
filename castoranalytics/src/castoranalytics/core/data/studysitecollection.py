class StudySiteCollection:
    def __init__(self, study_sites):
        self._study_sites_by_id = {}
        self._study_sites_by_name = {}
        self._study_sites_by_abbreviation = {}

    def load_by_id(self, study_sites):
        study_sites_by_id = {}
        for study_site in study_sites:
            study_sites_by_id[study_site.id()] = study_site
        return study_sites_by_id

    def load_by_name(self, study_sites):
        study_sites_by_name = {}
        for study_site in study_sites:
            study_sites_by_name[study_site.name()] = study_site
        return study_sites_by_name

    def load_by_abbreviation(self, study_sites):
        study_sites_by_abbreviation = {}
        for study_site in study_sites:
            study_sites_by_abbreviation[study_site.abbreviation()] = study_site
        return study_sites_by_abbreviation

    def all(self):
        return self._study_sites_by_id.values()
    
    def by_id(self, id):
        if id in self._study_sites_by_id.keys():
            return self._study_sites_by_id
        return None
    
    def by_name(self, name):
        if name in self._study_sites_by_name.keys():
            return self._study_sites_by_name
        return None
    
    def by_abbreviation(self, abbreviation):
        if abbreviation in self._study_sites_by_abbreviation.keys():
            return self._study_sites_by_abbreviation
        return None