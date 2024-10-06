import re

from sqlalchemy import Column, Integer, String, Boolean

from model.entity.book_validation import *
from model.entity.base import Base
from model.entity.product_validation import no_numbers, string_validator


class Product(Base):
    __tablename__ = 'product'

    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column(String, nullable=False)
    _brand = Column(String, nullable=False)
    _model = Column(String, nullable=False)
    _barcode = Column(String, nullable=False)
    _buy_price = Column(Integer, nullable=False)
    _sell_price = Column(Integer, nullable=False)


    def __init__(self,id, name, brand, model, barcode, buy_price, sell_price):
        self._id = id
        self._name = name
        self._brand = brand
        self._model = model
        self._barcode = barcode
        self._buy_price = buy_price
        self._sell_price = sell_price

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = no_numbers(name)

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = no_numbers(brand)

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = string_validator(model)

    def get_barcode(self):
        return self._barcode

    def set_barcode(self, barcode):
        self._barcode = string_validator(barcode)

    def get_buy_price(self):
        return self._buy_price

    def set_buy_price(self, buy_price):
        self._buy_price = positive_int(buy_price)

    def get_sell_price(self):
        return self._sell_price

    def set_sell_price(self, sell_price):
        self._sell_price = positive_int(sell_price)

    name = property(get_name, set_name)
    brand = property(get_brand, set_brand)
    model = property(get_model, set_model)
    barcode = property(get_barcode, set_barcode)
    buy_price = property(get_buy_price, set_buy_price)
    sell_price = property(get_sell_price, set_sell_price)
