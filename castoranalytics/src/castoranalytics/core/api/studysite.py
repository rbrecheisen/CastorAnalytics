class StudySite:
    def __init__(self, study_site_data):
        self._study_site_data = study_site_data

    def get_id(self):
        self._study_site_data['site_id']

    def get_abbreviation(self):
        self._study_site_data['abbreviation']

    def get_country_id(self):
        self._study_site_data['country_id']

    def get_nr_participants(self):
        return 0

    def get_average_completion_percentage(self):
        return 100