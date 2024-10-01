from model.entity.employee import Employee
from model.repository.crud_repository import CrudRepository


class EmployeeService:
    repo = CrudRepository(Employee)

    @classmethod
    def save(cls, employee):
        cls.repo.save(employee)

    @classmethod
    def edit(cls, employee):
        cls.repo.edit(employee)

    @classmethod
    def remove(cls, id):
        cls.repo.remove(id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    @classmethod
    def find_by(cls, by):
        return cls.repo.find_by(by)
