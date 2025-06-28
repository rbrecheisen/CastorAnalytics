class Loader:
    def __init__(self, credentials):
        self._credentials = credentials

    def credentials(self):
        return self._credentials