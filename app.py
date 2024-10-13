from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from controller.employee_controller import EmployeeController
from controller.user_controller import UserController
from model.entity.base import Base
from model.entity.book import Book
from model.entity.employee import Employee
from model.service.employee_service import EmployeeService
from view.employee_view import EmployeeView

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# ui = EmployeeView()
# emp = Employee(None, "ali", "alipour", 20)
# book = Book(None, "Python","mft",200)
#
# EmployeeService.save(emp)

# print(emp)
# print(book)

EmployeeController.save("ali", "alipour", 20)
emp = EmployeeController.find_by_id(1)[1]

UserController.save( "ali", "ali123456", emp)

u = UserController.find_by_id(1)
print(u)
# print(u.username)
# print(u.employee.name)