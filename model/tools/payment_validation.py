import re


class PaymentValidation:

    @staticmethod
    def person_validator(person, message):
        if type(person) == str and re.match(r"^[a-zA-Z\s]{2,20}$", person):
            return person
        else:
            raise ValueError(message)

    @staticmethod
    def account_int(account_id, message):
        if type(account_id) == int and re.match(r"^[0-9]{2,16}$", account_id):
            return account_id
        else:
            raise ValueError(message)

    @staticmethod
    def amount_int(amount, message):
        if type(amount) == int and re.match(r"^[0-9]+$", amount):
            return amount
        else:
            raise ValueError(message)
