from model.entity.employee import Employee
from model.service.employee_service import EmployeeService
from model.tools.decorators import exception_handling


class EmployeeController:    

    @classmethod
    @exception_handling
    def save(cls, name, family, age):
        emp = Employee(None, name, family, age)
        EmployeeService.save(emp)
        return  "Employee Saved"

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, age):
        emp = Employee(id, name, family, age)
        EmployeeService.edit(emp)
        return "Employee Edited"

    @classmethod
    @exception_handling
    def remove(cls, id):
        EmployeeService.remove(id)
        return "Employee Removed"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, EmployeeService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, EmployeeService.find_by_id(id)
