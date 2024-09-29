from model.entity.payment import Payment
from model.service.payment_service import PaymentService


class PaymentController:
    @classmethod
    def process_payment(cls, account_id, amount, person):
        try:
            pay = Payment(None, account_id, amount, person)
            PaymentService.process_payment(pay)
            return True, 'Payment Saved'
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit_payment(cls, id, account_id, amount, person):
        try:
            pay = Payment(id, account_id, amount, person)
            PaymentService.edit_payment(pay)
            return True, 'Payment Edited'
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove_payment(cls, id):
        try:
            PaymentService.remove_payment(id)
            return True, 'Payment Removed'
        except Exception as e:
            return False, str(e)

    @classmethod
    def get_all_payments(cls):
        try:
            return True, PaymentService.get_all_payments()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_payment_by_id(cls, id):
        try:
            return True, PaymentService.find_by_id(id)
        except Exception as e:
            return False, str(e)
