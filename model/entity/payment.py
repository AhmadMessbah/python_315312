from datetime import datetime


class Payment:
    # todo D Group: id, account, amount, date_time, person
    def __init__(self, id, account_id, amount, person):
        self.id = id
        self.account_id = account_int(account_id)
        self.amount = amount_int(amount)
        self.date_time = datetime.now()
        self.person = person_validator(person)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())

    def get_account_id(self):
        return self.account_id

    def set_account_id(self, account_id):
        self.account_id = account_int(account_id)

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount_int(amount)

    def get_person(self):
        return self.person

    def set_person(self, person):
        self.person = person_validator(person)

    account_id = property(get_account_id, set_account_id)
    amount = property(get_amount, set_amount)
    person = property(get_person, set_person)
    # if isinstance(date_time, datetime) else datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
