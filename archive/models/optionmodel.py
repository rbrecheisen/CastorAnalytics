from castoranalytics.models.model import Model


class OptionModel(Model):
    def __init__(self, name, label, idx):
        super(OptionModel, self).__init__()
        if not isinstance(name, str):
            raise RuntimeError(f'Argument "name" is not string but "{type(name)}"')
        if not isinstance(label, str):
            raise RuntimeError(f'Argument "label" is not string but "{type(label)}"')
        if not isinstance(idx, int):
            raise RuntimeError(f'Argument "idx" is not int but "{type(idx)}"')
        self._name = name
        self._label = label
        self._idx = idx

    def name(self):
        return self._name
    
    def label(self):
        return self._label
    
    def idx(self):
        return self._idx