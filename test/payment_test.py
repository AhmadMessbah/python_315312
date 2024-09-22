from model.entity.payment import Payment
from model.repository.payment_repository import PaymentRepository
from model.service.payment_service import PaymentService
from controller.payment_controller import PaymentController
from datetime import datetime


controller = PaymentController()

def test_process_payment():

    payment_id = None
    amount = 1000
    date_time = datetime.now()
    person = "Reza Rezaee"


    success, message = controller.process_payment(payment_id, amount, date_time, person)

    print(success, message)

test_process_payment()