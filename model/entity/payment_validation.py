import re

def person_validator(person):
    if type(person) == str and re.match(r"^[a-zA-Z0-9\s]{2,20}$", person):
        return person
    else:
        return False, "Error: Invalid Data For Person!"

def account_int(account):
    if type(account) == int and re.match(r"^[0-9]+$", account):
        return account
    else:
        return False, "Error: Invalid Data For Account!"