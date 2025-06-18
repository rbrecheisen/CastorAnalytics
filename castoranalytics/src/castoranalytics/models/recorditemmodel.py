from datetime import datetime

from castoranalytics.models.model import Model
from castoranalytics.models.fieldmodel import FieldModel


class RecordItemModel(Model):
    def __init__(self, name, value, field):
        super(RecordItemModel, self).__init__()
        if not isinstance(name, str):
            raise RuntimeError(f'Argument "name" is not string but "{type(name)}"')
        if not isinstance(value, str):
            raise RuntimeError(f'Argument "str_value" is not string but "{type(value)}"')
        if not isinstance(field, FieldModel):
            raise RuntimeError(f'Argument "field" is not of type "FieldModel" but "{type(field)}"')
        self._name = name
        self._value = value
        self._field = field

    def name(self):
        return self._name
    
    def value(self):
        if self._field.is_str():
            return self._value
        elif self._field.is_int():
            return int(self._value)
        elif self._field.is_float():
            return float(self._value)
        elif self._field.is_bool():
            return True if self._value == '1' or self._value.lower() == 'true' else False
        elif self._field.is_date():
            return datetime.strptime(self._value, self._field.date_format())
        raise RuntimeError('Unknown data type while retrieving value')