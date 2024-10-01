from model.entity.payment import Payment
from model.service.payment_service import PaymentService


class PaymentController:

    @classmethod
    def save(cls, account_id, amount, person):
        # payment entity setter
        try:
            pay = Payment(None, account_id, amount, person)
            PaymentService.save(id, pay, amount, person)
            return True, "Info: Payment Saved!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, account_id, amount, person):
        try:
            pay = Payment(id, account_id, amount, person)
            PaymentService.edit(pay, account_id, amount, person)
            return True, "Payment Has Been Edited!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            PaymentService.remove(id)
            return True, "Info: Payment Removed!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, PaymentService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, PaymentService.find_by_id(id)
        except Exception as e:
            return False, str(e)
