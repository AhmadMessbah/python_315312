class User:
    def __init__(self, id, account_id, amount, date_time, person):
        self.id = id


    def __repr__(self):
        return f"{self.__dict__}"
