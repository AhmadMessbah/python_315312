import re

from model.entity.employee import Employee
from model.service.employee_service import EmployeeService


class EmployeeController:    

    @classmethod
    def save(cls, name, family, age):
        try:
            emp = Employee(None, name, family, age)
            print("BEFORE ", emp)
            EmployeeService.save(emp)
            print("AFTER ", emp)
            return True, "Employee Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, age):
        try:
            emp = Employee(id, name, family, age)
            EmployeeService.edit(emp)
            return True, "Employee Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            EmployeeService.remove(id)
            return True, "Employee Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, EmployeeService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, EmployeeService.find_by_id(id)
        except Exception as e:
            return False, str(e)