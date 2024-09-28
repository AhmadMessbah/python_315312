import re

from model.entity.employee import Employee
from model.service.employee_service import EmployeeService


class EmployeeController:
    def __init__(self):
        self.service = EmployeeService()

    def save(self, name, family, age):
        # مدیریت خطا
        # پاسخ
        # اعتبارسنجی
        if re.match(r"^[a-zA-z\s]{2,20}$", name) and re.match(r"^[a-zA-z\s]{2,20}$", family):
            emp = Employee(None, name, family, age)
            error = self.service.save(emp)
            if not error:
                return True, "Info : Employee Saved"
            else:
                return False, error
        else:
            return False, "Error : Invalid Data"

    def edit(self, id, name, family, age):
        if re.match(r"^[a-zA-z\s]{2,20}$", name) and re.match(r"^[a-zA-z\s]{2,20}$", family):
            emp = Employee(id, name, family, age)
            error = self.service.edit(emp)
            if not error:
                return True, "Employee Edited"
            else:
                return False, error
        else:
            return False, "Invalid Data"

    def remove(self, id):
        error = self.service.remove(id)
        if not error:
            return True, "Employee Removed"
        else:
            return False, error

    def find_all(self):
        return self.service.find_all()
