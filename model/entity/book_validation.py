import re


def title_validator(title):
    if type(title) == str and re.match(r"^[a-zA-Z0-9\s]{2,30}$", title):
        return title

def author_validator(author):
    if type(author) == str and re.match(r"^[a-zA-Z\s]{2,30}$", author):
        return author


def positive_int(number):
    if type(number) == int and number > 0:
        return number
    else:
        return 0