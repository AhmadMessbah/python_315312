from datetime import datetime
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
                self.cursor.execute("update user_tbl set name=%s , family=%s,birth_date=%s,password=%s,username=%s,is_active=%s where name=%s",
                                    [user.name,user.family,user.birth_date,user.password,user.username,user.is_active])
                self.connection.commit()
                self.disconnect()

            def remove(self, user):
                self.connect()
                self.cursor.execute("delete from user_tbl where password=%s",[user.password])
                self.connection.commit()
                self.disconnect()


            def find_all(self, user):
                self.connect()
                self.cursor.execute("select * from user_tbl where password=%s",[user.password])
                user_list = self.cursor.fetchall()
                user_list=[User(*user) for user in user_list]
                self.disconnect()
                if user_list:
                    return user_list

            def find_user_by_username(self, username):
                self.connect()
                self.cursor.execute("select * from user_tbl where username=%s",[username])
                use=self.cursor.fetchone()
                self.disconnect()
                if use:User(*use)
                return use

