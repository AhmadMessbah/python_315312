import re


def id_validator(id):
    if type(id) == int and re.match(r"^[1-9]{7}$", id):
        return id
def name_validator(name):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", name):
        return name
def brand_validator(brand):
    if type(brand) == str and re.match(r"^[a-zA-Z1-9\s]{2,20}$", brand):
        return brand
def model_validator(model):
    if type(model) == str and re.match(r"^[a-zA-Z1-9\s]{2,20}$", model):
        return model
def barcode_validator(barcode):
    if type(barcode) == str and re.match(r"^[a-zA-Z1-9]{10}$", barcode):
        return barcode
def buy_sell_validator(buy_price, sell_price):
    if type(buy_price,sell_price) == int :
        return buy_price , sell_price
    else:
        return 0