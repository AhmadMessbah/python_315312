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

    def set_title(self, id):
        self._id = id_validator(id)

    def get_name(self  ):






    id = property(get_id, set_title)