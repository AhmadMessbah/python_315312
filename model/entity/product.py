from email.policy import default

from model.entity.base import Base
from model.tools.product_validation import Validation
from sqlalchemy import Column, Integer, String


class Product(Base):
    __tablename__ = "product_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _brand = Column("brand", String(20), nullable=False)
    _model = Column("model", String(20), nulable = False)
    _barcode = Column("barcode", String(20), nullable=False)
    _buy_price = Column("buy_price", Integer, default = 0)
    _sell_price = Column("sell_price", Integer, default = 0)

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
    def brand(self):
        return self._brand

    @brand.setter
    def family(self, brand):
        self._brand = Validation.brand_validator(brand, "Invalid Family")

    @property
    def model(self):
        return self._model

    @model.setter
    def age(self,model):
        self._model = Validation.brand_validator(model, "Invalid Model")

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        self._barcode = Validation.brand_validator(barcode, "Invalid Barcode")

    @property
    def buy_price(self):
        return self._buy_price

    @buy_price.setter
    def buy_price(self, buy_price):
        self._buy_price = Validation.buy_sell_validator(buy_price, "Invalid Buy Price")

    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, sell_price):
        self._sell_price = Validation.buy_sell_validator(sell_price, "Invalid Sell Price")