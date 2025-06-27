class Country:
    def __init__(self):
        self._id = None
        self._name = None
        self._code2 = None
        self._code3 = None

    def id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def code2(self):
        return self._code2
    
    def set_code2(self, code2):
        self._code2 = code2

    def code3(self):
        return self._code3
    
    def set_code3(self, code3):
        self._code3 = code3