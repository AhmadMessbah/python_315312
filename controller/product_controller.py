import re
from model.entity.product import Product
from model.service.product_service import ProductService
class ProductController:

    @classmethod
    def save(cls, name, brand, model, barcode, buy_price, sell_price):
        try:
            product = Product(None, name, brand, model, barcode, buy_price, sell_price)
            ProductService.save(product)
            return True, "Product Saved ʕ •ᴥ•ʔ"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, brand, model, barcode, buy_price, sell_price):
        try:
            product = Product(id, name, brand, model, barcode, buy_price, sell_price)
            error = ProductService.edit(product)
            return True ,"Product Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
            try:
                return True, "Product Removed"
            except Exception as e:
                return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, ProductService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, ProductService.find_by_id(id)
        except Exception as e:
            return False, str(e)