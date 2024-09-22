from model.entity.payment import Payment
from model.repository.payment_repository import PaymentRepository
from model.service.payment_service import PaymentService
from controller.payment_controller import PaymentController
from datetime import datetime


controller = PaymentController()

def test_process_payment():

    payment_id = None
    account = "1234"
    amount = 1000
    person = "Reza Rezaee"
    date_time = datetime.now()


    success, message = controller.process_payment(payment_id, amount, date_time, person)

    print(success, message)

test_process_payment()