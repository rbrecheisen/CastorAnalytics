class RecordItem:
    def __init__(self):
        self._name = None
        self._type = None
        self._value = None

    def name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def type(self):
        return self._type
    
    def set_type(self, type):
        self._type = type

    def value(self):
        return self._value
    
    def set_value(self, value):
        self._value = value