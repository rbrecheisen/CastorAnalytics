class CountryCollection:
    def __init__(self, countries):
        self._countries_by_id = {}
        self._countries_by_name = {}
        self._countries_by_two_digit_code = {}
        self._countries_by_three_digit_code = {}

    def load_by_id(self, countries):
        countries_by_id = {}
        for country in countries:
            countries_by_id[country.id()] = country
        return countries_by_id
    
    def load_by_name(self, countries):
        countries_by_name = {}
        for country in countries:
            countries_by_name[country.name()] = country
        return countries_by_name
    
    def load_by_two_digit_code(self, countries):
        countries_by_two_digit_code = {}
        for country in countries:
            countries_by_two_digit_code[country.two_digit_code()] = country
        return countries_by_two_digit_code
    
    def load_by_three_digit_code(self, countries):
        countries_by_three_digit_code = {}
        for country in countries:
            countries_by_three_digit_code[country.three_digit_code()] = country
        return countries_by_three_digit_code

    def all(self):
        return self._countries_by_id.values()
    
    def by_id(self, id):
        if id in self._countries_by_id.keys():
            return self._countries_by_id[id]
        return None
    
    def by_name(self, name):
        if name in self._countries_by_name.keys():
            return self._countries_by_name[name]
        return None
        
    def by_two_digit_code(self, two_digit_code):
        if two_digit_code in self._countries_by_two_digit_code.keys():
            return self._countries_by_two_digit_code[two_digit_code]
        return None
    
    def by_three_digit_code(self, three_digit_code):
        if three_digit_code in self._countries_by_three_digit_code.keys():
            return self._countries_by_three_digit_code[three_digit_code]
        return None