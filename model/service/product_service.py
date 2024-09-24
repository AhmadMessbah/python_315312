from model.repository.product_repository import ProductRepository
from model.entity.product import Product

class ProductService:
    def __init__(self):
        self.repo = ProductRepository()

    def save(self, product):
        if product.buy_price < product.sell_price:
            self.repo.save(product)
        else:
            return "Sell price should be greater than buy price !!!"

    def edit(self, product):
        if product.buy_price < product.sell_price:
            self.repo.edit(product)
        else:
            return "Sell price should be greater than buy price !!!"


    def remove(self, id):
        self.repo.remove(id)

    def find_all(self):
        return self.repo.find_all()


    def find_by_id(self, id):
        return self.repo.find_by_id(id)
