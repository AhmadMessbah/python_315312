from sqlalchemy.sql.sqltypes import BOOLEANTYPE

from model.entity.base import Base
from sqlalchemy import Column, Integer, String, Date, Boolean
from model.tools.user_validation import Validation

class User(Base):
    __tablename__ = "user_tbl"


    _id = Column("id", Integer , primary_key=True, autoincrement=True)
    _name = Column("name", String(30), nullable=False)
    _family = Column("family", String(30), nullable=False)
    _birth_date = Column("birth_date",Date)
    _username = Column("username", String(20), nullable=False)
    _password = Column("password", String(15), nullable=False)
    _is_active = Column("is_active", Boolean, default=True)


    def __init__(self, id, name, family, birth_date, username, password, is_active):
        self.id = id
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.username = username
        self.password = password
        self.is_active = is_active


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validation.name_validator(name, "Invlid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validation.family_validator(family, "Invalid Family")

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = Validation.birth_date_validator(birth_date, "Invalid Birth Date")

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
