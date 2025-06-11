import threading

from concurrent.futures import ThreadPoolExecutor

from castoranalytics.core.singleton import singleton
from castoranalytics.core.api.study import Study
from castoranalytics.core.api.studydetails import StudyDetails
from castoranalytics.core.api.studysite import StudySite
from castoranalytics.core.api.country import Country
from castoranalytics.core.logging import LogManager
from castoranalytics.core.cache import Cache
from castoranalytics.core.api.castorapiclient import CastorApiClient
from castoranalytics.core.utils import current_time_in_seconds, elapsed_time_in_seconds, duration

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
        start_time = current_time_in_seconds()
        countries = self._cache.get('countries')
        if countries:
            LOG.info(f'Core.get_countries() elapsed: {elapsed_time_in_seconds(start_time)}')
            return countries
        with CastorApiClient(self._client_id, self._client_secret, self._token_url, self._api_base_url) as client:
            countries = []
            for country_data in client.get_countries():
                countries.append(Country(country_data))
            self._cache.set('countries', countries)
            LOG.info(f'Core.get_countries() elapsed: {elapsed_time_in_seconds(start_time)}')
            return countries

    def get_studies(self):
        start_time = current_time_in_seconds()
        studies = self._cache.get('studies')
        if studies:
            LOG.info(f'Core.get_studies() elapsed: {elapsed_time_in_seconds(start_time)}')
            return studies
        with CastorApiClient(self._client_id, self._client_secret, self._token_url, self._api_base_url) as client:
            studies = []
            for study_data in client.get_studies():
                studies.append(Study(study_data))
            self._cache.set('studies', studies)
            LOG.info(f'Core.get_studies() elapsed: {elapsed_time_in_seconds(start_time)}')
            return studies
        
    def get_study(self, study_id):
        start_time = current_time_in_seconds()
        study = self._cache.get(f'studies/{study_id}')
        if study:
            LOG.info(f'Core.get_study() elapsed: {elapsed_time_in_seconds(start_time)}')
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
            LOG.info(f'Core.get_study() elapsed: {elapsed_time_in_seconds(start_time)}')
            return study
        
    def get_study_sites(self, study_id):
        start_time = current_time_in_seconds()
        study_sites = self._cache.get(f'studies/{study_id}/sites')
        if study_sites:
            LOG.info(f'Core.get_study_sites() elapsed: {elapsed_time_in_seconds(start_time)}')
            return study_sites
        with CastorApiClient(self._client_id, self._client_secret, self._token_url, self._api_base_url) as client:
            start_time2 = current_time_in_seconds()
            study_sites_data = client.get_study_sites(study_id)
            LOG.info(f'Core.get_study_sites() client.get_study_sites() elapsed: {elapsed_time_in_seconds(start_time2)}')
            start_time2 = current_time_in_seconds()
            participants = client.get_participants(study_id)
            LOG.info(f'Core.get_study_sites() client.get_participants() elapsed: {elapsed_time_in_seconds(start_time2)}')
            start_time2 = current_time_in_seconds()
            # Get participant site abbreviations
            participant_site_abbreviations = {}
            for participant in participants:
                participant_site_abbreviations[participant['participant_id']] = participant['_embedded']['site']['abbreviation']
            # Get participant progress
            participant_progress = client.get_participant_progress(study_id)
            LOG.info(f'Core.get_study_sites() client.get_participant_progress() elapsed: {elapsed_time_in_seconds(start_time2)}')
            # Calculate nr. records and form completion rates
            start_time2 = current_time_in_seconds()
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
            LOG.info(f'Core.get_study_sites() calculate completion rates elapsed: {elapsed_time_in_seconds(start_time2)}')
            # Update site info
            start_time2 = current_time_in_seconds()
            for study_site_data in study_sites_data:
                study_site_data['nr_records'] = 0
                if study_site_data['abbreviation'] in nr_records_per_site.keys():
                    study_site_data['nr_records'] = nr_records_per_site[study_site_data['abbreviation']]
                study_site_data['completion_rate'] = 0
                if study_site_data['abbreviation'] in completion_rates_per_site.keys():
                    study_site_data['completion_rate'] = completion_rates_per_site[study_site_data['abbreviation']] / float(study_site_data['nr_records']) if study_site_data['nr_records'] > 0 else 0
            LOG.info(f'Core.get_study_sites() site info updated elapsed: {elapsed_time_in_seconds(start_time2)}')
            study_sites = []
            for study_site_data in study_sites_data:
                study_sites.append(StudySite(study_site_data))
            self._cache.set(f'studies/{study_id}/sites', study_sites)
            LOG.info(f'Core.get_study_sites() elapsed: {elapsed_time_in_seconds(start_time)}')
            return study_sites    
        
    # ASYNCHRONOUS METHODS
        
    def get_countries_async(self, callback):
        self.run_background_task(self.get_countries, callback)

    def get_studies_async(self, callback):
        self.run_background_task(self.get_studies, callback)

    def get_study_async(self, callback, *args):
        self.run_background_task(self.get_study, callback, *args)

    def get_study_sites_async(self, callback, *args):
        self.run_background_task(self.get_study_sites, callback, *args)

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