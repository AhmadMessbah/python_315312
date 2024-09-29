import re

class ProductValidation:
    @staticmethod
    def id_validator(id,message):
        if type(id) == int and re.match(r"^[1-9]{7}$", id):
            return id
        else:
            return ValueError(message)

    @staticmethod
    def name_validator(name,message):
        if type(name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", name):
            return name
        else:
            return ValueError(message)

    @staticmethod
    def brand_validator(brand, message):
        if type(brand) == str and re.match(r"^[a-zA-Z1-9\s]{2,20}$", brand):
            return brand
        else:
            return ValueError(message)

    @staticmethod
    def model_validator(model, message):
        if type(model) == str and re.match(r"^[a-zA-Z1-9\s]{2,20}$", model):
            return model
        else:
            return ValueError(message)

    @staticmethod
    def barcode_validator(barcode, message):
        if type(barcode) == str and re.match(r"^[a-zA-Z1-9]{10}$", barcode):
            return barcode
        else:
            return ValueError(message)

    @staticmethod
    def buy_sell_validator(price, message):
        if type(price) == int :
            return price
        else:
            return ValueError(message)