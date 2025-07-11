import io
import csv

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

TOKEN_URL = 'https://data.castoredc.com/oauth/token'
API_BASE_URL = 'https://data.castoredc.com/api'


class CastorApiClient:
    def __init__(self, credentials):
        self._session = self.create_session(
            credentials.client_id(), credentials.client_secret(), TOKEN_URL)
        self._api_url = API_BASE_URL

    def create_session(self, client_id, client_secret, token_url):
        client = BackendApplicationClient(client_id=client_id)
        client_session = OAuth2Session(client=client)
        client_session.fetch_token(token_url=token_url, code=client_id, client_secret=client_secret)
        return client_session
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    # HELPERS

    def load_csv_data_as_dict(self, csv_data):
        dict_data = []
        for row in csv.DictReader(io.StringIO(csv_data), delimiter=';'):
            dict_data.append(row)
        return dict_data

    # COUNTRIES

    def countries(self):
        countries = []
        response = self._session.get(f'{self._api_url}/country')
        response.raise_for_status()
        response_data = response.json()
        for item in response_data.get('results', []):
            countries.append(item)
        # for item in countries:
        #     print(item)
        return countries
    
    # STUDIES
    
    def studies(self):
        studies = []
        response = self._session.get(f'{self._api_url}/study')
        response.raise_for_status()
        response_data = response.json()
        for study in response_data.get('_embedded', {}).get('study', {}):
            studies.append(study)
        # for item in studies:
        #     print(item)
        return studies
    
    def study(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}')
        response.raise_for_status()
        response_data = response.json()
        return response_data
    
    # SITES
    
    def number_of_sites(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/site?page=1')
        response.raise_for_status()
        response_data = response.json()
        return int(response_data.get('total_items', 0))

    def study_sites(self, study_id):
        study_sites, current_page = [], 1
        while True:
            new_sites, page_count = self.study_sites_by_page(study_id, current_page)
            if not new_sites:
                break
            study_sites.extend(new_sites)
            if current_page >= page_count:
                break
            current_page += 1
        # for item in study_sites:
        #     print(item)
        return study_sites
    
    def study_sites_by_page(self, study_id, page):
        response = self._session.get(f'{self._api_url}/study/{study_id}/site?page={page}')
        response.raise_for_status()
        response_data = response.json()
        sites = response_data.get('_embedded', {}).get('sites', [])
        page_count = response_data.get('page_count', 1)
        return sites, page_count
    
    def study_site(self, study_id, site_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/site/{site_id}')
        response.raise_for_status()
        response_data = response.json()
        return response_data

    def statistics(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/statistics')
        response.raise_for_status()
        response_data = response.json()
        return response_data
    
    # PARTICIPANTS
    
    def participants(self, study_id):
        participants, current_page = [], 1
        while True:
            new_participants, page_count = self.participants_by_page(study_id, current_page)
            if not new_participants:
                break
            participants.extend(new_participants)
            if current_page >= page_count:
                break
            current_page += 1
        return participants
    
    def participants_by_page(self, study_id, page):
        response = self._session.get(f'{self._api_url}/study/{study_id}/participant?page={page}')
        response.raise_for_status()
        response_data = response.json()
        new_participants = response_data.get('_embedded', {}).get('participants', [])
        page_count = response_data.get('page_count', 1)
        return new_participants, page_count
    
    # PARTICIPANT PROGRESS

    def participant_progress(self, study_id):
        participants_progress_data, current_page = [], 1
        while True:
            new_participant_progress_data, page_count = self.participant_progress_by_page(study_id, current_page)
            if not new_participant_progress_data:
                break
            participants_progress_data.extend(new_participant_progress_data)
            if current_page >= page_count:
                break
            current_page += 1
        return participants_progress_data
    
    def participant_progress_by_page(self, study_id, page):
        response = self._session.get(f'{self._api_url}/study/{study_id}/participant-progress/forms?page={page}')
        response.raise_for_status()
        response_data = response.json()
        new_participant_progress_data = response_data.get('_embedded', {}).get('participants', [])
        page_count = response_data.get('page_count', 1)
        return new_participant_progress_data, page_count

    # DATA

    def fields(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/export/structure')
        response.raise_for_status()
        return self.load_csv_data_as_dict(response.text)

    def optiongroups(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/export/optiongroups')
        response.raise_for_status()
        return response.text

    def records(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/export/data')
        response.raise_for_status()
        return response.text
