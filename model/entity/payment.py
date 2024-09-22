from datetime import datetime


class Payment:
    # todo D Group: id, account, amount, date_time, person
    def __init__(self, id, account_id, amount, person):
        self.id = id
        self.account_id = account_id
        self.amount = amount
        self.date_time = None
        self.person = person

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())

    # if isinstance(date_time, datetime) else datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
