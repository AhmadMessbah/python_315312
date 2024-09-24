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

    def edit_payment(self, id, account_id, amount, person):
        pay = Payment(id, account_id, amount, person)
        error = self.service.edit_payment(pay)
        if not error:
            return True, "Payment Has Been Edited!"
        else:
            return False, error

    def remove_payment(self, id):
        error = self.service.remove_payment(id)
        if not error:
            return True, "Payment Has Been Removed!"
        else:
            return False, error

    def find_payment_by_id(self, id):
        payment = self.service.find_payment_by_id(id)
        if payment:
            return "Payment Found!", payment
        else:
            return f"Payment With ID {id} Not Found!"

    def get_all_payments(self):
        return self.service.get_all_payments()
