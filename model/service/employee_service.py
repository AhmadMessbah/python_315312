from model.repository.employee_repository import EmployeeRepository


class EmployeeService:
    repo = EmployeeRepository()

    @classmethod
    def save(cls, employee):
        if 20 <= employee.age <= 30:
            cls.repo.save(employee)
        else:
            return ValueError("Age is not valid !!!")

    @classmethod
    def edit(cls, employee):
        if 20 <= employee.age <= 30:
            cls.repo.edit(employee)
        else:
            return ValueError("Age is not valid !!!")

    @classmethod
    def remove(cls, id):
        cls.repo.remove(id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)
