import re

from model.service.product_service import ProductService
from model.entity.product import Product


class ProductController:
    def __init__(self):
        self.service = ProductService()

    def save(self, id, name, brand, model, barcode, buy_price, sell_price):
            prd = Product(id, name, brand, model, barcode, buy_price, sell_price)
            error = self.service.save(prd)
            if not error:
                return True, "Info : Product Saved"
            else:
                return False, error


    def edit(self,id, name, brand, model, barcode, buy_price, sell_price):
            prd = Product(id, name, brand, model, barcode, buy_price, sell_price)
            error = self.service.edit(prd)
            if not error:
                return True, "Product Edited"
            else:
                return False, error


    def remove(self,id):
        error = self.service.remove(id)
        if not error:
            return True, "Product Removed"
        else:
            return False, error

    def find_all(self):
        return self.service.find_all()