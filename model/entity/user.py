from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import BOOLEANTYPE

from model.entity.base import Base
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from model.tools.user_validation import Validation

class User(Base):
    __tablename__ = "user_tbl"

    _id = Column("id", Integer , primary_key=True, autoincrement=True)
    _username = Column("username", String(20), nullable=False)
    _password = Column("password", String(15), nullable=False)
    _is_active = Column("is_active", Boolean, default=True)

    _employee_id = Column("employee_id", Integer, ForeignKey("employee_tbl.id") )
    employee = relationship("Employee")


    def __init__(self, id, username, password, is_active=True):
        self.id = id
        self.username = username
        self.password = password
        self.is_active = is_active
        self.employee = None


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = Validation.username_validator(username, "Invalid Username")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = Validation.password_validator(password, "Invalid Password")

    def get_is_active(self):
        return self._is_active

    def set_is_active(self, is_active):
        self._is_active = is_active
