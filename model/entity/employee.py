from model.tools.validation import Validation


class Employee:
    def __init__(self, id, name, family, age):
        self.id = id
        self.name = name
        self.family = family
        self.age = age

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        self._name = Validation.name_validator(name, "Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validation.family_validator(family, "Invalid Family")

    def to_tuple(self):
        return tuple(self.__dict__.values())

    def __repr__(self):
        return f"{self.__dict__}"