import re
from datetime import date


class Validation:
    @staticmethod
    def name_validator(name, message):
         if type(name) == str and re.match(r"^[a-zA-Z]{2,20}$", name):
             return name
         else:
             raise ValueError(message)
    @staticmethod
    def family_validator(family, message):
         if type(family) == str and re.match(r"^[a-zA-Z]{2,20}$", family):
            return family
         else:
           raise ValueError(message)

    @staticmethod
    def birth_date_validator(birth_date, message):
        if type(birth_date) == date:
           return birth_date
        else:
            raise ValueError(message)

    @staticmethod
    def username_validator(username, message):
       if  re.match(r"^[0-9a-zA-Z\s]{2,20}$", username):
        return username
       else:
          raise ValueError(message)

    @staticmethod
    def password_validator(password, message):
       if  re.match(r"^[0-9a-zA-Z\s]{8,20}$", password):
         return password
       else:
         raise ValueError(message)
