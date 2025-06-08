from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


class CastorApiClient:
    def __init__(self, client_id, client_secret, token_url, api_base_url):
        self._session = self.create_session(client_id, client_secret, token_url)
        self._api_url = api_base_url

    def create_session(self, client_id, client_secret, token_url):
        client = BackendApplicationClient(client_id=client_id)
        client_session = OAuth2Session(client=client)
        client_session.fetch_token(token_url=token_url, code=client_id, client_secret=client_secret)
        return client_session
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def get_countries(self):
        countries = []
        response = self._session.get(f'{self._api_url}/country')
        response.raise_for_status()
        response_data = response.json()
        for item in response_data.get('results', []):
            countries.append(item)
        # for item in countries:
        #     print(item)
        return countries
    
    def get_studies(self):
        studies = []
        response = self._session.get(f'{self._api_url}/study')
        response_data = response.json()
        for study in response_data.get('_embedded', {}).get('study', {}):
            studies.append(study)
        # for item in studies:
        #     print(item)
        return studies