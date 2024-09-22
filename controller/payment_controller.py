from model.entity.payment import Payment
from model.service.payment_service import PaymentService
import re


class PaymentController:
    def __init__(self):
        self.service = PaymentService()

    def process_payment(self, id, account_id, amount, person):
        # payment entity setter
        pay = Payment(None, account_id, amount, person)
        error = self.service.process_payment(pay)
        if not error:
            return True, "Info: Payment Saved!"
        else:
            return False, error


    def get_payment(self, id):
        payment = self.service.get_payment(id)
        if payment:
            return "Payment Found!", payment
        else:
            return f"Payment with ID {id} not found!"

    def get_all_payments(self):
        return self.service.get_all_payments()
