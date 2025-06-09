import io
import csv

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

    # HELPERS

    def load_csv_data_as_dict(self, csv_data):
        dict_data = []
        for row in csv.DictReader(io.StringIO(csv_data), delimiter=';'):
            dict_data.append(row)
        return dict_data

    # COUNTRIES

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
    
    # STUDIES
    
    def get_studies(self):
        studies = []
        response = self._session.get(f'{self._api_url}/study')
        response.raise_for_status()
        response_data = response.json()
        for study in response_data.get('_embedded', {}).get('study', {}):
            studies.append(study)
        # for item in studies:
        #     print(item)
        return studies
    
    def get_study(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}')
        response.raise_for_status()
        response_data = response.json()
        return response_data
    
    def get_number_of_sites(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/site?page=1')
        response.raise_for_status()
        response_data = response.json()
        return int(response_data.get('total_items', 0))

    def get_statistics(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/statistics')
        response.raise_for_status()
        response_data = response.json()
        return response_data
    
    # PARTICIPANTS
    
    def get_participants(self, study_id):
        participants, current_page = [], 1
        while True:
            response = self._session.get(f'{self._api_url}/study/{study_id}/participant?page={current_page}')
            response.raise_for_status()
            response_data = response.json()
            new_participants = response_data.get('_embedded', {}).get('participants', [])
            if not new_participants:
                break
            participants.extend(new_participants)
            if current_page >= response_data.get('page_count', 1):
                break
            current_page += 1
        return participants

    def get_participant_progress(self, study_id):
        participants_progress_data, current_page = [], 1
        while True:
            response = self._session.get(f'{self._api_url}/study/{study_id}/participant-progress/forms?page={current_page}')
            response.raise_for_status()
            response_data = response.json()
            new_participant_progress_data = response_data.get('_embedded', {}).get('participants', [])
            if not new_participant_progress_data:
                break
            participants_progress_data.extend(new_participant_progress_data)
            if current_page >= response_data.get('page_count', 1):
                break
            current_page += 1
        return participants_progress_data

    # DATA

    def get_fields(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/export/structure')
        response.raise_for_status()
        return self.load_csv_data_as_dict(response.text)

    def get_optiongroups(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/export/optiongroups')
        response.raise_for_status()
        return response.text

    def get_records(self, study_id):
        response = self._session.get(f'{self._api_url}/study/{study_id}/export/data')
        response.raise_for_status()
        return response.text
