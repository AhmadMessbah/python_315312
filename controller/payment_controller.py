from model.entity.payment import Payment
from model.service.payment_service import PaymentService


class PaymentController:
    @classmethod
    def __init__(cls):
        cls.service = PaymentService()

    @classmethod
    def process_payment(cls, id, account_id, amount, person):
        # payment entity setter
        pay = Payment(None, account_id, amount, person)
        try:
            return True, 'Payment Saved'
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit_payment(cls, id, account_id, amount, person):
        pay = Payment(id, account_id, amount, person)
        try:
            return True, 'Payment Edited'
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove_payment(cls, id):
        try:
            return True, 'Payment Removed'
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_payment_by_id(cls, id):
        payment = cls.service.find_payment_by_id(id)
        try:
            return True, 'Payment Found', payment
        except Exception as e:
            return False, str(e), f"Payment {id} not found"

    @classmethod
    def get_all_payments(cls):
        try:
            return True, cls.service.get_all_payments()
        except Exception as e:
            return False, str(e)
