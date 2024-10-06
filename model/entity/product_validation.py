import re


def no_numbers(name):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{2,30}$", name):
        return name

def string_validator(string) :
    if type(string) == str and re.match(r"^{2,30}$"):
        return string


def positive_int(number):
    if type(number) == int and number > 0:
        return number
    else:
        return 0