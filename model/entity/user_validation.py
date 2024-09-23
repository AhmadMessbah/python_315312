import re

def id_validator(id):
    if type(id) == int and re.match("^[1-9]{10}$", id):
        return id

def name_validator(name):
    if type(name) == str and re.match("^[a-zA-Z]{2,20}$", name):
        return name

def family_validator(family):
    if type(family) == str and re.match("^[a-zA-Z]{2,20}$", family):
        return family

def birth_date_validator(birth_date):
    if type(birth_date) == int and re.match("^[0-9]{4,10}$", birth_date):
        return birth_date

def username_validator(username):
    if re.match("^[0-9a-zA-Z\s]{2,20}$", username):
        return username

def password_validator(password):
    if re.match("^[0-9a-zA-Z\s]{8,20}$", password):
        return password
