# python cant find it(error > no module named product validator)
from pefile import PrologEpilogOpSetFP

from model.entity.product_validation import *
from model.tools.validation import Validation


class Product:
    def __init__(self, id, name, brand, model,barcode,buy_price,sell_price):
        self.id = id
        self.name = name
        self.brand = brand
        self.model = model
        self.barcode = barcode
        self.buy_price = buy_price
        self.sell_price = sell_price

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.id = Validation.id_validator(id, "Invalid id")

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = Validation.name_validator(name, "Invalid Name")

    @property
    def brand(self):
        return self.brand

    @brand.setter
    def brand(self, brand):


    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model_validator(model)

    def get_barcode(self):
        return self._barcode

    def set_barcode(self, barcode):
        self._barcode = barcode_validator(barcode)

    def get_buy_price(self):
        return self._buy_price

    def set_buy_price(self, buy_price):
        self._buy_price = buy_sell_validator(buy_price)

    def get_sell_price(self):
        return self._sell_price

    def set_sell_price(self, sell_price):
        self._sell_price = buy_sell_validator(sell_price)




