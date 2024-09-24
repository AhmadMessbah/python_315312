## service/payment_service.py - Creator: power0matin
from model.repository.payment_repository import PaymentRepository
from model.entity.payment import Payment

class PaymentService:
    def __init__(self):
        self.payment_repository = PaymentRepository()

        # ایجاد پرداخت
    def process_payment(self, account, amount, person):
        id = len(self.payment_repository.payments) + 1
        new_payment = Payment(id, account, amount, person)

        # ذخیره پرداخت در repository
        return self.payment_repository.save(new_payment)

    def find_payment_by_id(self, id):
        payment = self.payment_repository.find_by_id(id)
        if payment:
            return payment
        return f"Payment with ID {id} not found."

    def get_all_payments(self):
        payments = self.payment_repository.find_all()
        if payments:
            return payments
        else:
            return "Payments not found !!"

    def edit_payment(self, id, amount=None, date_time=None, person=None):
        payment = self.payment_repository.find_by_id(id)
        if not payment:
            return f"Payment with ID {id} not found."

        if amount is not None:
            payment.amount = amount
        if date_time is not None:
            payment.date_time = date_time
        if person is not None:
            payment.person = person

        self.payment_repository.edit(payment)
        return f"Payment with ID {id} updated successfully."

    def remove_payment(self, id):
        payment = self.payment_repository.find_by_id(id)
        if not payment:
            return f"Payment with ID {id} not found."

        self.payment_repository.remove(id)
        return f"Payment with ID {id} removed successfully."
