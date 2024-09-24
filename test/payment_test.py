from model.entity.payment import Payment


payment = Payment(1, 12345, 500, "Reza Rezaee")

print(payment)

print(payment.to_tuple())
