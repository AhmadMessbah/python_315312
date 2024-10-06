# python cant find it(error > no module named product validator)
#from pefile import PrologEpilogOpSetFP

# from model.entity.product_validation import *
from model.tools.product_validation import ProductValidation
from product_validation import *


class Product:
    def __init__(self, id, name, brand, model,barcode,buy_price,sell_price):
        self.id = id
        self.name = name
        self.brand = brand
        self.model = model
        self.barcode = barcode
        self.buy_price = buy_price
        self.sell_price = sell_price

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = no_numbers(name)

    def get_brand(self):
        return self.brand
    def set_brand(self, brand):
        self.brand = no_numbers(brand)

    def get_model(self):
        return self.model
    def set_model(self, model):
        self.model = string_validator(model)

    def get_barcode(self):
        return self.barcode
    def set_barcode(self, barcode):
        self.barcode = string_validator(barcode)

    def get_buy_price(self):
        return self.buy_price
    def set_buy_price(self, buy_price):
        self.buy_price = positive_int(buy_price)

    def get_sell_price(self):
        return self.sell_price
    def set_sell_price(self, sell_price):
        self.sell_price = positive_int(sell_price)

    name = property(get_name, set_name)
    brand = property(get_brand, set_brand)
    model = property(get_model, set_model)
    barcode = property(get_barcode, set_barcode)
    buy_price = property(get_buy_price, set_buy_price)
    sell_price = property(get_sell_price, set_sell_price)