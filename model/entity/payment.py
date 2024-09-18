from datetime import datetime

class Payment:
    def __init__(self, payment_id, amount, date_time, person):
        self.payment_id = payment_id
        self.amount = amount
        self.date_time = date_time if isinstance(date_time, datetime) else datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
        self.person = person

    def __str__(self):
        return f"Payment(ID: {self.payment_id}, Amount: {self.amount}, Date: {self.date_time}, Person: {self.person})"

    def to_dict(self):
        return {
            "payment_id": self.payment_id,
            "amount": self.amount,
            "date_time": self.date_time.strftime("%Y-%m-%d %H:%M:%S"),
            "person": self.person
        }