class BaseCommand:
    def __init__(self, args):
        self._args = args

    def get_args(self):
        return self._args

    def execute(self):
        raise NotImplementedError('Not implemented')