import re

from model.entity.user import User
from model.service.user_service import User


class UserController:

    @classmethod
    def save(cls, name, family, birth_date, username, password):
        try:
            us = User(None, name, family, birth_date,username,password)
            UserService.save(us)
            return True, "User Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, birth_date, username, password):
        try:
            us = User(id, name, family, birth_date, username, password)
            UserService.edit(us)
            return True, "User Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            UserService.remove(id)
            return True, "User Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, UserService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, UserService.find_by_id(id)
        except Exception as e:
            return False, str(e)
