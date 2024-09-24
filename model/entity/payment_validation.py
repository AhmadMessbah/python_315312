import re


def person_validator(person):
    if type(person) == str and re.match(r"^[a-zA-Z0-9\s]{2,20}$", person):
        return person
    else:
        return False, "Error: Invalid Data For Person!"


def account_int(account_id):
    if type(account_id) == int and re.match(r"^[0-9]{2,16}$", account_id):
        return account_id
    else:
        return False, "Error: Invalid Data For Account!"


def amount_int(amount):
    if type(amount) == int and re.match(r"^[0-9]+$", amount):
        return amount
    else:
        return False, "Error: Invalid Data For Amount!"
