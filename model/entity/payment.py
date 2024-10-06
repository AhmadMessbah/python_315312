from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime
from model.entity.base import Base
from model.tools.payment_validation import PaymentValidation

class Payment:
    __tablename__ = "payment_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _account_id = Column("account_id", Integer, nullable=False)
    _amount = Column("amount", Float, nullable=False)
    _date_time = Column("date_time", DateTime, default=datetime.now)
    _person = Column("person", String(30), nullable=False)

    def __init__(self, id, account_id, amount, person):
        self.person = person
        self.id = id
        self.account_id = account_id
        self.amount = amount
        self.person = person
        self.date_time = datetime.now()

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


