from user_validation import *

class User:
    def __init__(self, id,name,family,birth_date,username,password,is_active):
        self.id = id
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.username = username
        self.password = password
        self.is_active = is_active

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id_validator(id)

    def get_name(self):
        return self._name
            
    def set_name(self, name):
        self._name = name_validator(name)

    def get_family(self):
        return self._family
    
    def set_family(self, family):
        self._family = family_validator(family)



    id = property(get_id, set_id)
    name= property(get_name, set_name)
    family = property(get_family, set_family)