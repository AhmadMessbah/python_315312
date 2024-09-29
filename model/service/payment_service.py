from model.repository.payment_repository import PaymentRepository
from model.entity.payment import Payment


# save, edit, remove, find_all, find_by_id

class PaymentService:
    repo = PaymentRepository()

    @classmethod
    def process_payment(cls, account, amount, person):
        new_payment = Payment(id, account, amount, person)

        return cls.repo.save(new_payment)

    @classmethod
    def find_by_id(cls, id):
        return repo.find_by_id(id)


    @classmethod
    def get_all_payments(cls):
        payment_repository = PaymentRepository()
        try:
            payments = payment_repository.find_all()
            return payments
        except:
            return "Payments not found!!!"


    @classmethod
    def edit_payment(cls, id, amount=None, date_time=None, person=None):
        payment_repository = PaymentRepository()
        try:
            payment = payment_repository.find_by_all(id)
            payment_repository.edit(payment)
            return f"Payment with ID {id} updated."
        except:
            return f"Payment with ID {id} not found."


    @classmethod
    def remove_payment(cls, id):
        payment_repository = PaymentRepository()
        try:
            payment_repository.remove(id)
            return f"Payment with ID {id} removed"
        except:
            return f"Payment with ID {id} not found"
