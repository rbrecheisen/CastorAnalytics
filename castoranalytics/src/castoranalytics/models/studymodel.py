from castoranalytics.models.model import Model
from castoranalytics.models.fieldmodel import FieldModel
from castoranalytics.models.optiongroupmodel import OptionGroupModel
from castoranalytics.models.studysitemodel import StudySiteModel


class StudyModel(Model):
    def __init__(self, id, name):
        super(StudyModel, self).__init__()
        if not isinstance(id, str):
            raise RuntimeError(f'Argument "id" not a string but "{type(id)}"')
        if not isinstance(name, str):
            raise RuntimeError(f'Argument "name" not a string but "{type(id)}"')
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
        if not isinstance(site, StudySiteModel):
            raise RuntimeError('Object is not of type "StudySiteModel"')
        if site.id() not in self._sites.keys():
            self._sites[site.id()] = site
        else:
            raise RuntimeError(f'Site with ID "{site.id()}" already added to study')
        
    def site(self, id):
        if not id in self._sites.keys():
            raise RuntimeError(f'Site with ID "{id}" not found')
        return self._sites[id]
    
    def nr_sites(self):
        return len(self._sites.keys())
    
    # FIELDS

    def add_field(self, field):
        if not isinstance(field, FieldModel):
            raise RuntimeError('Object is not of type "FieldModel"')

    def field(self, id):
        if id not in self._fields.keys():
            raise RuntimeError(f'Field with ID "{id}" does not exist')
        return self._fields[id]

    def nr_fields(self):
        return len(self._fields.keys())
    
    # OPTION GROUPS

    def add_option_group(self, option_group):
        if not isinstance(option_group, OptionGroupModel):
            raise RuntimeError('Object is not of type "OptionGroupModel"')
        if option_group.id() not in self._option_groups.keys():
            self._option_groups[option_group.id()] = option_group
        else:
            raise RuntimeError(f'Option group with ID "{option_group.id()}" already added to study')

    def option_group(self, id):
        if id not in self._option_groups.keys():
            raise RuntimeError(f'Option group with ID "{id}" does not exist')
        return self._option_groups[id]

    def nr_option_groups(self):
        return len(self._option_groups.keys())