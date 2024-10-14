from controller.payment_controller import PaymentController
from model.entity.payment import Payment

print(PaymentController.save(1, 12345567,  "Reza Rezaee"))
#payment = Payment(1, 12345, 500, "Reza Rezaee")

#print(payment)

#print(payment.to_tuple())
