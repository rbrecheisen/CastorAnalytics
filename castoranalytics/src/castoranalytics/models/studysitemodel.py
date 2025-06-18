from castoranalytics.models.model import Model
from castoranalytics.models.countrymodel import CountryModel
from castoranalytics.models.recordmodel import RecordModel


class StudySiteModel(Model):
    def __init__(self, id, name, abbreviation, country):
        super(StudySiteModel, self).__init__()
        if not isinstance(id, str):
            raise RuntimeError(f'Argument "id" is not string but "{type(id)}"')
        if not isinstance(name, str):
            raise RuntimeError(f'Argument "name" is not string but "{type(name)}"')
        if not isinstance(abbreviation, str):
            raise RuntimeError(f'Argument "abbreviation" is not string but "{type(abbreviation)}"')
        if not isinstance(country, CountryModel):
            raise RuntimeError(f'Argument "country" is not type "CountryModel" but "{type(country)}"')
        self._id = id
        self._name = name
        self._abbreviation = abbreviation
        self._country = country
        self._records = {}

    def id(self):
        return self._id
    
    def name(self):
        return self._name
    
    def abbreviation(self):
        return self._abbreviation
    
    def country(self):
        return self._country

    def add_record(self, record):
        if not isinstance(record, RecordModel):
            raise RuntimeError('Object is not of type "RecordModel"')
        if record.id() not in self._records.keys():
            self._records[record.id()] = record
        else:
            raise RuntimeError(f'Record with ID "{record.id()}" already added to study site')

    def record(self, id):
        if id not in self._records.keys():
            raise RuntimeError(f'Record with ID "{id}" does not exist')
        return self._records[id]

    def nr_records(self):
        return len(self._records.keys())