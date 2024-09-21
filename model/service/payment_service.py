## service/payment_service.py - Creator: power0matin
from model.repository.payment_repository import PaymentRepository
from model.entity.payment import Payment

class PaymentService:
    def __init__(self):
        self.payment_repository = PaymentRepository()

        # ایجاد پرداخت
    def process_payment(self, account, amount, person):
        payment_id = len(self.payment_repository.payments) + 1
        new_payment = Payment(payment_id, account, amount, person)

        # ذخیره پرداخت در repository
        return self.payment_repository.save(new_payment)

    def find_payment_by_id(self, payment_id):
        payment = self.payment_repository.find_by_id(payment_id)
        if payment:
            return payment
        return f"Payment with ID {payment_id} not found."

    def get_all_payments(self):
        payments = self.payment_repository.get_all()
        if payments:
            return payments
        else:
            return "Payments not found !!"
