class StudySite:
    def __init__(self):
        self._id = None
        self._name = None
        self._country = None
        self._abbrevation = None
        self._records = None

    def id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def country(self):
        return self._country
    
    def set_country(self, country):
        self._country = country

    def abbreviation(self):
        return self._abbrevation
    
    def set_abbreviation(self, abbreviation):
        self._abbrevation = abbreviation

    def records(self):
        return self._records
    
    def set_records(self, records):
        self._records = records