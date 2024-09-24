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

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id_validator(id)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name_validator(name)

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand_validator(brand)

    def get_model(self):
        return self.model

    def set_model(self, model):
        self._model = model_validator(model)

    def get_barcode(self):
        return self.barcode

    def set_barcode(self, barcode):
        self.barcode = barcode_validator(barcode)

    def get_buy_price(self):
        return self.buy_price

    def set_buy_price(self, buy_price):
        self.buy_price = buy_sell_validator(buy_price)

    def get_sell_price(self):
        return self.sell_price

    def set_sell_price(self, sell_price):
        self.sell_price = buy_sell_validator(sell_price)


    id= property(get_id, set_id)
    name = property(get_name, set_name)
    brand = property(get_brand, set_brand)
    model = property(get_model,set_model)
    barcode = property(get_barcode,set_barcode)
    buy_price = property(get_buy_price,set_buy_price)
    sell_price = property(get_sell_price,set_sell_price)

