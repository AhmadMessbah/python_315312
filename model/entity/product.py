from model.entity.base import Base
from model.tools.product_validation import ProductValidation
from sqlalchemy import Column, Integer, String


class Product(Base):
    __tablename__ = "product_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30), nullable=False)
    _brand = Column("brand", String(30), nullable=False)
    _model = Column("model", String(30), nullable=False)
    _barcode = Column("barcode", Integer, nullable=False)
    _buy_price = Column("buy_price", Integer)
    _sell_price = Column("sell_price", Integer)
    def __init__(self, id, name, brand, model,barcode,buy_price,sell_price):
        self.id = id
        self.name = name
        self.brand = brand
        self.model = model
        self.barcode = barcode
        self.buy_price = buy_price
        self.sell_price = sell_price



    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = ProductValidation.id_validator(id, "Invalid id")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = ProductValidation.name_validator(name, "Invalid Name")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = ProductValidation.brand_validator(brand, "Invalid brand")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._brand = ProductValidation.model_validator(model, "Invalid model")

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        self._barcode = ProductValidation.barcode_validator(barcode, "Invalid barcode")

    @property
    def buy_price(self):
        return self._buy_price

    @buy_price.setter
    def buy_price(self, buy_price):
        self._buy_price = ProductValidation.buy_sell_validator(buy_price, "Invalid buy price")

    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, sell_price):
        self._sell_price = ProductValidation.buy_sell_validator(sell_price, "Invalid sell price")


# test




