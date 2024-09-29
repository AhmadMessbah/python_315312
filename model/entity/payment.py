from datetime import datetime
import re
from model.tools.payment_validation import PaymentValidation


class Payment:
    # todo D Group: id, account, amount, date_time, person
    def __init__(self, id, account_id, amount, person):
        self.id = id
        self.account_id = account_id
        self.amount = amount
        self.date_time = datetime.now()

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = PaymentValidation.account_int(account_id, "Invalid Account Id")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = PaymentValidation.amount_int(amount, "Invalid Amount")

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, person):
        self._person = PaymentValidation.person_validator(person, "Invalid Person")

# if isinstance(date_time, datetime) else datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
