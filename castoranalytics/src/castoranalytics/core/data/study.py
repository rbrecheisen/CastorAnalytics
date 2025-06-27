class Study:
    def __init__(self):
        self._id = None
        self._name = None
        self._fields = None
        self._optiongroups = None
        self._sites = None

    def id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def fields(self):
        return self._fields
    
    def set_fields(self, fields):
        self._fields = fields

    def optiongroups(self):
        return self._optiongroups
    
    def set_optiongroups(self, optiongroups):
        self._optiongroups = optiongroups

    def sites(self):
        return self._sites
    
    def set_sites(self, sites):
        self._sites = sites