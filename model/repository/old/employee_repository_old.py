import mysql.connector

from model.entity.employee import Employee


# save, edit, remove, find_all(), find_by_id()
class EmployeeRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="office_db"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, employee):
        self.connect()

        self.cursor.execute("insert into employee_tbl (name,family,age) values (%s,%s,%s)",
                            [employee.name, employee.family, employee.age])
        self.connection.commit()
        self.disconnect()

    def edit(self, employee):
        self.connect()
        self.cursor.execute("update employee_tbl set name=%s,family=%s,age=%s where id=%s",
                            [employee.name, employee.family, employee.age, employee.id])
        self.connection.commit()
        self.disconnect()

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from employee_tbl where id=%s", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from employee_tbl")
        emp_list = self.cursor.fetchall()
        emp_list = [Employee(*emp) for emp in emp_list]
        self.disconnect()
        if emp_list:
            return emp_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from employee_tbl where id=%s", [id])
        emp = self.cursor.fetchone()
        self.disconnect()
        if emp:
            emp = Employee(*emp)
            return emp
