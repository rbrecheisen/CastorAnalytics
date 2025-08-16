from castoranalytics.core.loaders.loader import Loader
from castoranalytics.core.castorapiclient import CastorApiClient
from castoranalytics.core.data.country import Country
from castoranalytics.core.data.countrycollection import CountryCollection


class CountryLoader(Loader):
    def __init__(self, credentials):
        super(CountryLoader, self).__init__(credentials)

    def load(self):
        # Notify listeners of progress
        with CastorApiClient(self.credentials()) as client:
            countries = []
            for country in client.countries():
                country_data = Country()
                country_data.set_id(country['country_id'])
                country_data.set_name(country['country_name'])
                country_data.set_two_digit_code(country['country_cca2'])
                country_data.set_three_digit_code(country['country_cca3'])
                countries.append(country_data)
            country_collection = CountryCollection(countries)
            return country_collection