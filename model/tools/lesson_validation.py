import re


class Validation:
    @staticmethod
    def title_validator(title, message):
        if type(title) == str and re.match(r"^[a-zA-Z\s]{2,20}$", title):
            return title
        else:
            raise ValueError(message)


