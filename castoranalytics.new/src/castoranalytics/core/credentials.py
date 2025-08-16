from castoranalytics.core.singleton import singleton


@singleton
class Credentials:
    def __init__(self):
        self._client_id = None
        self._client_secret = None

    def client_id(self):
        return self._client_id
    
    def set_client_id(self, client_id):
        self._client_id = client_id
    
    def client_secret(self):
        return self._client_secret
    
    def set_client_secret(self, client_secret):
        self._client_secret = client_secret