class Study:
    def __init__(self):
        self._id = None
        self._name = None

    def id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f'Study(id={self.id()}, name={self.name()})'