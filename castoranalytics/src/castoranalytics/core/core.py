import json
import hashlib
import threading

from concurrent.futures import ThreadPoolExecutor

from castoranalytics.core.singleton import singleton
from castoranalytics.core.api.study import Study
from castoranalytics.core.api.studydetails import StudyDetails
from castoranalytics.core.api.country import Country
from castoranalytics.core.logging import LogManager
from castoranalytics.core.cache import Cache
from castoranalytics.core.api.castorapiclient import CastorApiClient

LOG = LogManager()


@singleton
class Core:
    def __init__(self):
        self._client_id = None
        self._client_secret = None
        self._token_url = None
        self._api_base_url = None
        self._executor = ThreadPoolExecutor(max_workers=4)
        self._callbacks_lock = threading.Lock()
        self._callbacks = {}
        self._cache = Cache()

    def update_settings(self, client_id, client_secret, token_url, api_base_url):
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_url = token_url
        self._api_base_url = api_base_url

    def ready(self):
        return self._client_id is not None and self._client_secret is not None and self._token_url is not None and self._api_base_url is not None
    
    def get_countries(self):
        countries = self._cache.get('countries')
        if countries:
            return countries
        with CastorApiClient(self._client_id, self._client_secret, self._token_url, self._api_base_url) as client:
            countries = []
            for country_data in client.get_countries():
                countries.append(Country(country_data))
            self._cache.set('countries', countries)
            return countries

    def get_studies(self):
        studies = self._cache.get('studies')
        if studies:
            return studies
        with CastorApiClient(self._client_id, self._client_secret, self._token_url, self._api_base_url) as client:
            studies = []
            for study_data in client.get_studies():
                studies.append(Study(study_data))
            self._cache.set('studies', studies)
            return studies
        
    def get_study(self, study_id):
        study = self._cache.get(f'studies/{study_id}')
        if study:
            return study
        with CastorApiClient(self._client_id, self._client_secret, self._token_url, self._api_base_url) as client:
            study_data = client.get_study(study_id)
            study_statistics = client.get_statistics(study_id)
            fields = client.get_fields(study_id)
            study_data['nr_sites'] = client.get_number_of_sites(study_id)
            study_data['nr_participants'] = study_statistics['records']['total_count']
            study_data['nr_fields'] = len(fields)
            study = StudyDetails(study_data)
            self._cache.set(f'studies/{study_id}', study)
            return study
        
    def get_study_sites(self, study_id):
        study_sites = self._cache.get(f'studies/{study_id}/sites')
        if study_sites:
            return study_sites
        with CastorApiClient(self._client_id, self._client_secret, self._token_url, self._api_base_url) as client:
            sites = self.get_sites(study_id)
            participants = self.get_participants(study_id)
            # Get participant site abbreviations
            participant_site_abbreviations = {}
            for participant in participants:
                participant_site_abbreviations[participant['participant_id']] = participant['_embedded']['site']['abbreviation']
            # Get participant progress
            participant_progress = self.get_participant_progress(study_id)
            # Calculate nr. records and form completion rates
            nr_records_per_site = {}
            completion_rates_per_site = {}
            for item in participant_progress:
                site_abbreviation = participant_site_abbreviations[item['participant_id']]
                # Calculate number of records/participants
                if site_abbreviation not in nr_records_per_site.keys():
                    nr_records_per_site[site_abbreviation] = 0
                nr_records_per_site[site_abbreviation] += 1
                # Calculate completion rate
                if site_abbreviation not in completion_rates_per_site.keys():
                    completion_rates_per_site[site_abbreviation] = 0
                cummulative_progress = 0
                for form in item['forms']:
                    cummulative_progress += int(form['progress'])
                completion_rate = cummulative_progress / float(len(item['forms']))
                completion_rates_per_site[site_abbreviation] += completion_rate
            # Update site info
            for site in sites:
                site['nr_records'] = 0
                if site['abbreviation'] in nr_records_per_site.keys():
                    site['nr_records'] = nr_records_per_site[site['abbreviation']]
                site['completion_rate'] = 0
                if site['abbreviation'] in completion_rates_per_site.keys():
                    site['completion_rate'] = completion_rates_per_site[site['abbreviation']] / float(site['nr_records']) if site['nr_records'] > 0 else 0
            self._cache.set(f'studies/{study_id}/sites', sites)
            return sites    
        
    # ASYNCHRONOUS METHODS
        
    def get_countries_async(self, callback):
        self.run_background_task(self.get_countries, callback)

    def get_studies_async(self, callback):
        self.run_background_task(self.get_studies, callback)

    def get_study_async(self, callback, *args):
        self.run_background_task(self.get_study, callback, *args)

    # HELPERS

    def run_background_task(self, func, callback, *args, **kwargs):
        future = self._executor.submit(func, *args, **kwargs)
        with self._callbacks_lock:
            self._callbacks[future] = callback
        future.add_done_callback(self.handle_task_done)

    def handle_task_done(self, future):
        result, error = None, None
        try:
            result = future.result()
        except Exception as e:
            error = e
        with self._callbacks_lock:
            callback = self._callbacks.pop(future, None)
        if callback:
            callback(result, error)