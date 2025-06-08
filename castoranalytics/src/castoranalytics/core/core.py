import threading

from concurrent.futures import ThreadPoolExecutor

from castoranalytics.core.singleton import singleton
from castoranalytics.core.api.study import Study
from castoranalytics.core.api.country import Country
from castoranalytics.core.api.castorapiclient import CastorApiClient


@singleton
class Core:
    def __init__(self, client_id, client_secret, token_url, api_base_url):
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_url = token_url
        self._api_base_url = api_base_url
        self._countries = None
        self._studies = None
        self._executor = ThreadPoolExecutor(max_workers=4)
        self._callbacks_lock = threading.Lock()
        self._callbacks = {}

    def get_countries(self):
        if self._countries:
            return self._countries
        with CastorApiClient(self._client_id, self._client_secret, self._token_url, self._api_base_url) as client:
            self._countries = []
            for country_data in client.get_countries():
                self._countries.append(Country(country_data))
            return self._countries

    def get_studies(self):
        if self._studies:
            return self._studies
        with CastorApiClient(self._client_id, self._client_secret, self._token_url, self._api_base_url) as client:
            self._studies = []
            for study_data in client.get_studies():
                self._studies.append(Study(study_data))
            return self._studies
        
    def get_countries_async(self, callback):
        self.run_background_task(self.get_countries, callback)

    def get_studies_async(self, callback):
        self.run_background_task(self.get_studies, callback)
        
    def run_background_task(self, func, callback):
        future = self._executor.submit(func)
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