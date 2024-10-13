from model.entity.user import User
from model.service.user_service import UserService
from model.tools.decorators import exception_handling


class UserController:

    @classmethod
    @exception_handling
    def save(cls, username, password, employee):
        user = User(None,  username, password)
        user.employee = employee
        UserService.save(user)
        return "User Saved"

    @classmethod
    @exception_handling
    def edit(cls, id,  username, password, employee):
        user = User(id, username, password)
        user.employee = employee
        UserService.edit(user)
        return "User Edited"

    @classmethod
    @exception_handling
    def remove(cls, id):
        UserService.remove(id)
        return "User Removed"

    @classmethod
    @exception_handling
    def find_all(cls):
        return UserService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return UserService.find_by_id(id)
