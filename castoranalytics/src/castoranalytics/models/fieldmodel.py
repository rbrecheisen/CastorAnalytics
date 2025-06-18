from enum import Enum

from castoranalytics.models.model import Model


class FieldModel(Model):
    class Type(Enum):
        STRING = 0
        INT = 1
        FLOAT = 2
        BOOLEAN = 3
        DATE = 4

    def __init__(self, id, name, label, data_type, date_format=None):
        super(FieldModel, self).__init__()
        if not isinstance(id, str):
            raise RuntimeError(f'Argument "id" not string but "{type(id)}"')
        if not isinstance(name, str):
            raise RuntimeError(f'Argument "name" not string but "{type(name)}"')
        if not isinstance(label, str):
            raise RuntimeError(f'Argument "label" not string but "{type(label)}"')
        if data_type < 0 or data_type > 4:
            raise RuntimeError(f'Argument "data_type" outside range')
        if data_type == 4 and date_format is None:
            raise RuntimeError(f'Argument "date_format" cannot be None for a DATE type')
        self._id = id
        self._name = name
        self._label = label
        self._data_type = data_type
        self._date_format = date_format

    def id(self):
        return self._id
    
    def name(self):
        return self._name
    
    def label(self):
        return self._label
    
    def is_str(self):
        return self._data_type == FieldModel.Type.STRING
    
    def is_int(self):
        return self._data_type == FieldModel.Type.INT
    
    def is_float(self):
        return self._data_type == FieldModel.Type.FLOAT
    
    def is_bool(self):
        return self._data_type == FieldModel.Type.BOOLEAN
    
    def is_date(self):
        return self._data_type == FieldModel.Type.DATE
    
    def date_format(self):
        return self._date_format