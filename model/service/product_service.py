from model.repository.old.product_repository import ProductRepository


class ProductService:
    repo = ProductRepository()

    @classmethod
    def save(cls, product):
        try:
            if product.buy_price < product.sell_price:
                cls.repo.save(product)
        except:
            raise ValueError("Sell price should be greater than buy price !!!")

    @classmethod
    def edit(cls, product):
        try:
            if product.buy_price < product.sell_price:
                cls.repo.edit(product)
        except:
            raise ValueError("Sell price should be greater than buy price !!!")


    @classmethod
    def remove(cls, _id):
        cls.repo.remove(_id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.repo.find_by_id(_id)
