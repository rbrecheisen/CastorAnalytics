from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


class CastorApiClient:
    def __init__(self, token_url, api_base_url, client_id, client_secret):
        self._session = self.create_session(client_id, client_secret, token_url)
        self._api_base_url = api_base_url

    def create_session(self, client_id, client_secret, token_url):
        client = BackendApplicationClient(client_id=client_id)
        client_session = OAuth2Session(client=client)
        client_session.fetch_token(token_url=token_url, code=client_id, client_secret=client_secret)
        return client_session
    
    def close_session(self):
        self._session.close()