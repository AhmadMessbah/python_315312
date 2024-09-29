from model.repository.payment_repository import PaymentRepository as repo
from model.entity.payment import Payment


# save, edit, remove, find_all, find_by_id

class PaymentService:


    @classmethod
    def save(cls, account, amount, person):
        new_payment = Payment(id, account, amount, person)
        return cls.repo.save(new_payment)
    
    @classmethod
    def edit(cls, id, amount, date_time, person):
        try:
            payment = repo.find_by_all(id)
            repo.edit(payment)
            return f"Payment with ID {id} updated."
        except:
            return f"Payment with ID {id} not found."

    @classmethod
    def remove(cls, id):
        try:
            repo.remove(id)
            return f"Payment with ID {id} removed"
        except:
            return f"Payment with ID {id} not found"

    @classmethod
    def find_all(cls):
        try:
            payments = repo.find_all()
            return payments
        except:
            return "Payments not found !!!"

    @classmethod
    def find_by_id(cls, id):
        return repo.find_by_id(id)