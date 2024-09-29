from model.entity.payment import Payment
from model.service.payment_service import PaymentService


class PaymentController:
#    def __init__(self):
#        self.service = PaymentService()

    @classmethod
    def process_payment(cls, id, account_id, amount, person):
        # payment entity setter
        try:
            pay = Payment(None, account_id, amount, person)
            PaymentService.process_payment(pay)
            return True, "Info: Payment Saved!"
        except Exception as e:
            return False, str(e)

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
