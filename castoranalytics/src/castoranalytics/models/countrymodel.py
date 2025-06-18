from castoranalytics.models.model import Model
from castoranalytics.models.recorditemmodel import RecordItemModel


class CountryModel(Model):
    def __init__(self, id, name, tld_code, two_digit_code, three_digit_code):
        super(CountryModel, self).__init__()
        if not isinstance(id, str):
            raise RuntimeError(f'Argument "id" is not string but "{type(id)}"')
        if not isinstance(name, str):
            raise RuntimeError(f'Argument "name" is not string but "{type(id)}"')
        if not isinstance(tld_code, str):
            raise RuntimeError(f'Argument "tld_code" is not string but "{type(id)}"')
        if not isinstance(two_digit_code, str):
            raise RuntimeError(f'Argument "two_digit_code" is not string but "{type(id)}"')
        if not isinstance(three_digit_code, str):
            raise RuntimeError(f'Argument "three_digit_code" is not string but "{type(id)}"')
        self._id = id
        self._name = name
        self._tld_code = tld_code
        self._two_digit_code = two_digit_code
        self._three_digit_code = three_digit_code

    def id(self):
        return self._id
    
    def name(self):
        return self._name
    
    def tld_code(self):
        return self._tld_code
    
    def two_digit_code(self):
        return self._two_digit_code
    
    def three_digit_code(self):
        return self._three_digit_code