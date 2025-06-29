class StudySite:
    def __init__(self):
        self._id = None
        self._name = None
        self._country_id = None
        self._abbrevation = None

    def id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def country_id(self):
        return self._country_id
    
    def set_country_id(self, country_id):
        self._country_id = country_id

    def abbreviation(self):
        return self._abbrevation
    
    def set_abbreviation(self, abbreviation):
        self._abbrevation = abbreviation

    def __str__(self):
        return f'StudySite(id={self.id()}, name={self.name()}, country_id={self.country_id()}, abbreviation={self.abbreviation()})'