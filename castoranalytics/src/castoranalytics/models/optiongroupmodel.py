from castoranalytics.models.model import Model
from castoranalytics.models.optionmodel import OptionModel


class OptionGroupModel(Model):
    def __init__(self, id, name):
        super(OptionGroupModel, self).__init__()
        if not isinstance(id, str):
            raise RuntimeError(f'Argument "id" is not string but "{type(id)}"')
        if not isinstance(name, str):
            raise RuntimeError(f'Argument "name" is not string but "{type(name)}"')
        self._id = id
        self._name = name
        self._options = {}

    def id(self):
        return self._id
    
    def name(self):
        return self._name
    
    def add_option(self, option):
        if not isinstance(option, OptionModel):
            raise RuntimeError('Object is not of type "OptionModel"')
        if option.name() not in self._options.keys():
            self._options[option.name()] = option
        else:
            raise RuntimeError(f'Option with name "{option.name()}" already added to option group')
        
    def option(self, name):
        if not name in self._options.keys():
            raise RuntimeError(f'Option with name "{name}" not found')
        return self._options[name]
    
    def nr_options(self):
        return len(self._options.keys())