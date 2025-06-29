class Country:
    def __init__(self):
        self._id = None
        self._name = None
        self._two_digit_code = None
        self._three_digit_code = None

    def id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def two_digit_code(self):
        return self._two_digit_code
    
    def set_two_digit_code(self, two_digit_code):
        self._two_digit_code = two_digit_code

    def three_digit_code(self):
        return self._three_digit_code
    
    def set_three_digit_code(self, three_digit_code):
        self._three_digit_code = three_digit_code