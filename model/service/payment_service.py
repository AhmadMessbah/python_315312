# service/payment_service.py - Creator: power0matin
from repository.payment_repository import PaymentRepository
from entity.payment import Payment


class PaymentService:
    def __init__(self):
        self.payment_repository = PaymentRepository()

    def process_payment(self, account, amount, person):
        # ایجاد پرداخت به صورت مستقیم
        payment_id = len(self.payment_repository.payments) + 1
        new_payment = Payment(payment_id, account, amount, person)

        # ذخیره پرداخت جدید در repository
        saved_payment = self.payment_repository.save(new_payment)

        return saved_payment

    def get_payment(self, payment_id):
        pass

    def get_all_payments(self):
        pass
