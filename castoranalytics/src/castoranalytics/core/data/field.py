from enum import Enum


class Field:
    class Type(Enum):
        INT = 0
        FLOAT = 1
        BOOLEAN = 2
        STRING = 3
        OPTIONGROUP = 4
        DATE = 5
        DATETIME = 6
        YEAR = 7

    def __init__(self):
        self._id = None
        self._name = None
        self._type = None
        self._options = {}

    def id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def type(self):
        return self._type
    
    def set_type(self, type):
        self._type = type

    def options(self):
        self._options
        
    def set_options(self, options):
        self._options = options