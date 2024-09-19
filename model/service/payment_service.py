# service/payment_service.py - Creator: power0matin

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
        payment = self.payment.retrieve_by_id(payment_id)
        if payment:
            return payment
        else:
            return f"Payment with ID {payment_id} not found"

    def get_all_payments(self):
        payments = self.payment_repository.get_all()
        if payments:
            return payments
        else:
            return "Payments not found"
