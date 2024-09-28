import re

from user_validation import *


class User:
    def __init__(self, id, name, family,birth_date,username,password,is_active):
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
        return self._pages

    def set_family(self, family):
        self._family = family_validator(family)

    def get_birth_date(self):
        return self._birth_date

    def set_birth_date(self, birth_date):
        self._birth_date = positive_int(birth_date)

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = positive_int(username)

    def get_is_active(self):
         return self._is_active

    def set_is_active(self, is_active):
        self._is_active = boolian(is_active)



    id = property(get_id, set_id)
    name = property(get_name, set_name)
    family = property(get_family, set_family)
    birth_date = property(get_birth_date, set_birth_date)
    username = property(get_username, set_username)
    password = property(get_password, set_password)
    is_active = property(get_is_active, set_is_active)



