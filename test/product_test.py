from numpy.ma.extras import apply_along_axis


class product:
    def __init__(self, id, name, brand, model, barcod, buy_price, sell_price):
        self.id = id
        self.name = name
        self.brand = brand
        self.model = model
        self.barcod = barcod
        self.buy_price = buy_price
        self.sell_price = sell_price

    def __repr__(self):
        return f"{self.__dict__}"

id = 1
name = "aaa"
brand = "bbb"
model = "ccc"
barcod = 1234567890
buy_price = 10
sell_price = 20

print(tuple(product))

