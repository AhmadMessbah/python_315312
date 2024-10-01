from model.entity.user import User
from model.repository.crud_repository import CrudRepository


class UserService:
    repo = CrudRepository(User)

    @classmethod
    def save(cls, user):
        cls.repo.save(user)

    @classmethod
    def edit(cls, user):
        cls.repo.edit(user)

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
