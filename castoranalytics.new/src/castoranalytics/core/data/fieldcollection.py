from castoranalytics.core.data.collection import Collection


class FieldCollection(Collection):
    def __init__(self, fields):
        self._fields_by_id = self.load_by_id(fields)
        self._fields_by_name = self.load_by_name(fields)

    def load_by_id(self, fields):
        pass

    def load_by_name(self, fields):
        pass

    def all(self):
        pass

    def by_id(self, id):
        pass

    def by_name(self, name):
        pass

    def size(self):
        return len(self.all())