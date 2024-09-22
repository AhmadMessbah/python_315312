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

    def set_name(self, author):
        self._name = name_validator(name)

    def get_brand(self):
        return self._brand

    def set_pages(self, pages):
        self._brand = brand_validator(brand)

    def get_model(self):
        return self._model


    # title = property(get_title, set_title)
    # author = property(get_author, set_author)
    # pages = property(get_pages, set_pages)
