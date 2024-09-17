from model.repository.employee_repository import EmployeeRepository


class EmployeeService:
    def __init__(self):
        self.repo = EmployeeRepository()

    def save(self, employee):
        if 20 <= employee.age <=30:
            self.repo.save(employee)
        else:
            return "Age is not valid !!!"

    def edit(self, employee):
        if 20 <= employee.age <=30:
            self.repo.edit(employee)
        else:
            return "Age is not valid !!!"


    def remove(self, id):
        self.repo.remove(id)


    def find_all(self):
        return self.repo.find_all()


    def find_by_id(self, id):
        return self.repo.find_by_id(id)
