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


#def person_validator(person):
 #   if isinstance(person, str) and re.match(r"^[a-zA-Z0-9\s]{2,20}$", person):
  #      return person
   # else:
    #    raise ValueError("Error: Invalid Data For Person!")


#def account_int(account_id):
 #   if isinstance(account_id, int) and 2 <= len(str(account_id)) <= 16:
 #       return account_id
 #   else:
 #       raise ValueError("Error: Invalid Data For Account!")


#def amount_int(amount):
 #   if isinstance(amount, int) and amount >= 0:
 #       return amount
 #   else:
 #      raise ValueError("Error: Invalid Data For Amount!")
