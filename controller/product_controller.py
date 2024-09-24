import re
from model.entity.product import Product
from model.service.product_service import ProductService

class ProductController:
    def __init__(self):
        self.service = ProductService()

    def save(self, name, brand, model, barcode, buy_price, sell_price):
        # مدیریت خطا
        #پاسخ
        # اعتبارسنجی
        if (re.match(r"^[a-zA-Z\s]{2,20}$", name) and
            re.match(r"^[a-zA-Z\s]{2,20}$", brand) and
            re.match(r"^[a-zA-Z0-9\s]{2,20}$", model) and
            re.match(r"^\d{10}$", barcode) and
            type(buy_price, (int, float)) and buy_price >= 0 and
            type(sell_price, (int, float)) and sell_price >= 0):

            product = Product(None, name, brand, model, barcode, buy_price, sell_price)
            error = self.service.save(product)
            if not error:
                return True, "Info: Product Saved"
            else:
                return False, error
        else:
            return False, "Error: Invalid Data!!!"

    def edit(self, id, name, brand, model, barcode, buy_price, sell_price):
        if (re.match(r"^[a-zA-Z\s]{2,20}$", name) and
            re.match(r"^[a-zA-Z\s]{2,20}$", brand) and
            re.match(r"^[a-zA-Z0-9\s]{2,20}$", model) and
            re.match(r"^\d{12}$", barcode) and
            type(buy_price, (int, float)) and buy_price >= 0 and
            type(sell_price, (int, float)) and sell_price >= 0):

            product = Product(id, name, brand, model, barcode, buy_price, sell_price)
            error = self.service.edit(product)
            if not error:
                return True, "Product Edited"
            else:
                return False, error
        else:
            return False, "Invalid Data!!!"

    def remove(self, id):
        error = self.service.remove(id)
        if not error:
            return True, "Product Removed"
        else:
            return False, error

    def find_all(self):
        return self.service.find_all()
