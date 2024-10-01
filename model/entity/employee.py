from model.entity.base import Base
from model.tools.validation import Validation
from sqlalchemy import Column, Integer, String


class Employee(Base):
    __tablename__ = "employee_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20),nullable=False)
    _age = Column("age", Integer, default=0)

    def __init__(self, id, name, family, age):
        self.id = id
        self.name = name
        self.family = family
        self.age = age

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
        self._name = Validation.name_validator(name, "Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validation.family_validator(family, "Invalid Family")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


