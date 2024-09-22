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

    def save(self, payment):
        self.connect()
        self.cursor.execute("insert into payment_tbl (amount, date, person) values (%s,%s,%s)",
                            [payment.amount, payment.date_time, payment.person])
        self.connection.commit()
        self.disconnect()

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from payment_tbl where id=%s", [id])
        self.connection.commit()
        self.disconnect()

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from payment_tbl where id=%s", [id])
        emp = self.cursor.fetchone()
        self.disconnect()
        if emp:
            emp = Payment(*emp)
            return emp

