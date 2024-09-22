import re

from model.service.product_service import ProductService
from model.entity.product import Product


class ProductController:
    def __init__(self):
        self.service = ProductService()

    def save(self, id, name, brand, model, barcode, buy_price, sell_price):
        # مدیریت خطا
        # پاسخ
        # اعتبارسنجی
        if (re.match(r"^[1-9]{7}$", id)
        and re.match(r"^[a-zA-z\s]{2,20}$", name)
        and re.match(r"^[a-zA-z\s]{2,20}$", brand)
        and re.match(r"^[a-zA-z\s]{2,20}$", model)
        and re.match(r"^[1-9a-zA-Z]{20}$", barcode)
        and type(buy_price) == int and type(sell_price) == int):
            prd = Product(id, name, brand, model, barcode, buy_price, sell_price)
            error = self.service.save(prd)
            if not error:
                return True, "Info : Product Saved"
            else:
                return False, error
        else:
           return False, "Error : Invalid Data"


    def edit(self,id, name, brand, model, barcode, buy_price, sell_price):
        if (re.match(r"^[1-9]{7}$", id)
        and re.match(r"^[a-zA-z\s]{2,20}$", name)
        and re.match(r"^[a-zA-z\s]{2,20}$", brand)
        and re.match(r"^[a-zA-z\s]{2,20}$", model)
        and re.match(r"^[1-9a-zA-Z]{20}$", barcode)
        and type(buy_price) == int and type(sell_price) == int):
            prd = Product(id, name, brand, model, barcode, buy_price, sell_price)
            error = self.service.edit(prd)
            if not error:
                return True, "Product Edited"
            else:
                return False, error
        else:
            return False, "Invalid Data"


    def remove(self,id):
        error = self.service.remove(id)
        if not error:
            return True, "Product Removed"
        else:
            return False, error

    def find_all(self):
        return self.service.find_all()