from model.entity.payment import Payment
from model.service.payment_service import PaymentService
import re


class PaymentController:
    def __init__(self):
        self.service = PaymentService()

    def process_payment(self, payment_id, amount, date_time, person):
        if re.match(r"^[a-zA-Z\s]{2,20}$", person):
            pay = Payment(None, amount, date_time, person)
            error = self.service.process_payment(pay)
            if not error:
                return True, "Info: Payment Saved!"
            else:
                return False, error
        else:
            return False, "Error: Invalid Data!"

    def get_payment(self, payment_id):
        payment = self.service.get_payment(payment_id)
        if payment:
            return "Payment Found!", payment
        else:
            return f"Payment with ID {payment_id} not found!"

    def get_all_payments(self):
        return self.service.get_all_payments()
