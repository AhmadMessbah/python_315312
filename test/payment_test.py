from model.entity.payment import Payment
from model.repository.crud_repository import CrudRepository
from model.service.payment_service import PaymentService

payment_repo = CrudRepository(Payment)
payment_service = PaymentService()

# saving a payment
payment = Payment(account=12345567, amount=500, person="Reza Rezaee")
saved_payment = payment_service.save(payment)
print("Saved Payment:", saved_payment)

# editing a payment
payment.amount = 1000
edited_payment = payment_service.edit(payment)
print("Edited Payment:", edited_payment)

# removing a payment
removed_id = payment_service.remove(payment.id)
print("Removed Payment ID:", removed_id)

# finding all payments
all_payments = payment_service.find_all()
print("All Payments:", all_payments)

# finding a payment by ID
found_payment = payment_service.find_by_id(payment.id)
print("Found Payment by ID:", found_payment)

# finding payments by account
found_payments = payment_service.find_by(account=12345567)
print("Found Payments by Account:", found_payments)