from model.entity.payment import Payment
from model.repository.crud_repository import CrudRepository

class PaymentService:
    repo = CrudRepository(Payment)

    @classmethod
    def save(cls,id, account, amount, person):
        new_payment = Payment(id, account, amount, person)
        return cls.repo.save(new_payment)

    @classmethod
    def edit(cls, id, amount, date_time, person):
        try:
            payment = cls.repo.find_by_id(id)
            cls.repo.edit(payment)
            return f"Payment with ID {id} updated."
        except:
            return f"Payment with ID {id} not found."

    @classmethod
    def remove(cls, id):
        try:
            cls.repo.remove(id)
            return f"Payment with ID {id} removed"
        except:
            return f"Payment with ID {id} not found"

    @classmethod
    def find_all(cls):
        try:
            payments = cls.repo.find_all()
            return payments
        except:
            return "Payments not found !!!"

    @classmethod
    def find_by_id(cls, id):
        try:
            cls.repo.find_by_id(id)
            return f"Payment with ID {id} found."
        except:
            return f"Payment with ID {id} not found"
