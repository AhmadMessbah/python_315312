import mysql.connector

from model.entity.payment import Payment


class PaymentRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="payment_db"
        )
        self.cursor = self.connection.cursor()


def disconnect(self):
    self.cursor.close()
    self.connection.close()
