from castoranalytics.models.model import Model
from castoranalytics.models.exceptions.studysitenotfoundexception import StudySiteNotFoundException
from castoranalytics.models.exceptions.studysitealreadyaddedexception import StudySiteAlreadyAddedException


class StudyModel(Model):
    def __init__(self, id, name):
        super(StudyModel, self).__init__()
        self._id = id
        self._name = name
        self._fields = {}
        self._option_groups = {}
        self._sites = {}

    # GETTERS

    def id(self):
        return self._id
    
    def name(self):
        return self._name
    
    # SITES

    def add_site(self, site):
        if site.id() not in self._sites.keys():
            self._sites[site.id()] = site
        else:
            raise StudySiteAlreadyAddedException(f'Site with ID {site.id()} already added to study')
        
    def site(self, id):
        if not id in self._sites.keys():
            raise StudySiteNotFoundException(f'Site with ID {id} not found')
        return self._sites[id]
    
    def nr_sites(self):
        return len(self._sites.keys())
    
    # FIELDS

    def add_field(self, field):
        pass

    def field(self, id):
        pass

    def nr_fields(self):
        return len(self._fields.keys())
    
    # OPTION GROUPS

    def add_option_group(self, option_group):
        pass

    def option_group(self, id):
        pass

    def nr_option_groups(self):
        return len(self._option_groups.keys())