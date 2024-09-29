from model.repository.payment_repository import PaymentRepository
from model.entity.payment import Payment

class PaymentService:
    
    
    def __init_(self):
        self.payment_repository = PaymentRepository()

        # ایجاد پرداخت
    @classmethod
    def process_payment(cls, account, amount, person):
        id = len(cls.payment_repository.payments) + 1
        new_payment = Payment(id, account, amount, person)

        return cls.payment_repository.save(new_payment)

    @classmethod
    def find_payment_by_id(cls, id):
        payment_repository = PaymentRepository()
        try:
            payment = payment_repository.find_by_id(id)
            return payment
        except:
            return f"Payment with ID {id} not found." 
        
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
            payment = payment_repository.find_all(id)
            payment_repository.edit(payment)
            return f"Payment with ID {id} updated."
        except:
            return f"Payment with ID {id} not found."
        
    @classmethod        
    def remove_payment(self, id):
        payment_repository = PaymentRepository()
        try:
            payment_repository.remove(id)
            return f"Payment with ID {id} removed"
        except:
            return f"Payment with ID {id} not found"