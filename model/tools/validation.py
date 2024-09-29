import re


class Validation:
    @staticmethod
    def name_validator(name, message):
        if type(name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", name):
            return name
        else:
            raise ValueError(message)



    @staticmethod
    def family_validator(family, message):
        if type(family) == str and re.match(r"^[a-zA-Z\s]{2,20}$", family):
            return family
        else:
            raise ValueError(message)
