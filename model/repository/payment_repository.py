from datetime import datetime

import mysql.connector

from model.entity.payment import Payment


class PaymentRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="mft_db"
        )
        self.cursor = self.connection.cursor()
    
    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, payment):
        self.connect()
        self.cursor.execute("insert into payment_tbl (account_id, amount, date_time, person) values (%s,%s,%s,%s)",
                            [payment.account_id, payment.amount, datetime.now(), payment.person])
        self.connection.commit()
        self.disconnect()

    def edit(self, payment):
        self.connect()
        self.cursor.execute("update payment_tbl set account_id=%s, amount=%s, date_time=%s, person=%s where id=%s",
                            [payment.account_id, payment.amount, datetime.now(), payment.person, payment.id])
        self.connection.commit()
        self.disconnect()

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from payment_tbl where id=%s", [id])
        self.connection.commit()
        self.disconnect()


    def find_all(self, id):
        self.connect()
        self.cursor.execute("select * from payment_tbl")
        payment_list = self.cursor.fetchall()
        self.disconnect()
        if payment_list:
            return [Payment(*pay) for pay in payment_list]

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from payment_tbl where id=%s", [id])
        emp = self.cursor.fetchone()
        self.disconnect()
        if emp:
            return Payment(*emp)

# tst