from castoranalytics.models.model import Model
from castoranalytics.models.recorditemmodel import RecordItemModel


class RecordModel(Model):
    def __init__(self, id):
        super(RecordModel, self).__init__()
        if not isinstance(id, str):
            raise RuntimeError(f'Argument "id" is not string but "{type(id)}"')
        self._id = id
        self._items = {}

    def id(self):
        return self._id

    def add_item(self, item):
        if not isinstance(item, RecordItemModel):
            raise RuntimeError(f'Object is not of type "RecordItemModel"')
        if item.name() not in self._items.keys():
            self._items[item.name()] = item
        else:
            raise RuntimeError(f'Record item with name "{item.name()}" already added to record')
        
    def item(self, name):
        if name not in self._items.keys():
            raise RuntimeError(f'Record item with name "{name}" does not exist')
        return self._items[name]