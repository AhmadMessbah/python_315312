# python cant find it(error > no module named product validator)
from pefile import PrologEpilogOpSetFP

# from model.entity.product_validation import *
from model.tools.product_validation import ProductValidation



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
        self.id = ProductValidation.id_validator(id, "Invalid id")

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = ProductValidation.name_validator(name, "Invalid Name")

    @property
    def brand(self):
        return self.brand

    @brand.setter
    def brand(self, brand):
        self.brand = ProductValidation.brand_validator(brand, "Invalid brand")

    @property
    def model(self):
        return self.model

    @model.setter
    def model(self, model):
        self.brand = ProductValidation.model_validator(model, "Invalid model")

    @property
    def barcode(self):
        return self.barcode

    @barcode.setter
    def barcode(self, barcode):
        self.barcode = ProductValidation.barcode_validator(barcode, "Invalid barcode")

    @property
    def buy_price(self):
        return self.buy_price

    @buy_price.setter
    def buy_price(self, buy_price):
        self.buy_price = ProductValidation.buy_sell_validator(buy_price, "Invalid buy price")

    @property
    def sell_price(self):
        return self.sell_price

    @sell_price.setter
    def sell_price(self, sell_price):
        self.sell_price = ProductValidation.buy_sell_validator(sell_price, "Invalid sell price")




