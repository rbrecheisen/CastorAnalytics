class Record:
    def __init__(self):
        self._id = None
        self._items = None

    def id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def items(self):
        return self._items
    
    def set_items(self, items):
        self._items = items