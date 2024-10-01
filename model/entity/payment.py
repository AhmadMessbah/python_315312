from datetime import datetime
import re
from model.tools.payment_validation import PaymentValidation
from sqlalchemy import Column, Integer, String

class Payment:
    # todo D Group: id, account, amount, date_time, person
    __tablename__ = "payment_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _account_id = Column("account_id", Integer , primary_key=True, autoincrement=True)
    _amount = Column("amount", Integer , primary_key=True, autoincrement=True)
    _person = Column("person", String(20), nullable=False)

    def __init__(self, id, account_id, amount, person):
        self.id = id
        self.account_id = account_id
        self.amount = amount
        self.person = person

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
