import mysql.connector


class UserRepository:
    pass
def connect(self):
    self.connection = mysql.connector.connect(
      host="localhost",
        user="root",
        passwd="root123",
        database="office_db"
    )
    self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

        def save(self, user):
            self.connect()
            self.cursor.execute( "insert into user_tbl (name,family,birth_date,password,username,is_active) values(%s,%s,%s,%s,%s,%s)",
            [user.name,user.family,user.birth_date,user.password,user.username,user.is_active])
            self.connection.commit()
            self.cursor.disconnect()

            def edit(self, user):
                self.connect()
                self.cursor.execute("update user_tbl set name=%s , family=%s,birth_date=%s,password=%s,username=%s,is_active=%s where name=%s",)
