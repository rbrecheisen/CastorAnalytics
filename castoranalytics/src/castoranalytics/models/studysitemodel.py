from castoranalytics.models.model import Model
from castoranalytics.models.exceptions.recordalreadyaddedexception import RecordAlreadyAddedException
from castoranalytics.models.exceptions.recordnotfoundexception import RecordNotFoundException


class StudySiteModel(Model):
    def __init__(self, id, name, abbreviation, country):
        super(StudySiteModel, self).__init__()
        self._id = id
        self._name = name
        self._abbreviation = abbreviation
        self._country = country
        self._records = {}

    def has_record(self, record):
        return r

    def add_record(self, record):
        if record.id() not in self._records.keys():
            self._records[record.id()] = record
        else:
            raise RecordAlreadyAddedException(f'Record with ID {record.id()} already added to study site')

    def record(self, id):
        if id not in self._records.keys():
            raise RecordNotFoundException(f'Record with ID {id} does not exist')
        return self._records[id]

    def nr_records(self):
        return len(self._records.keys())