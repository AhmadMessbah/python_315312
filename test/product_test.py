from controller.product_controller import ProductController
controller = ProductController()
from model.entity.product import Product
print(controller.save("ban","boom","dsh",1234567891,2000,300))
prod = Product("1234567","DB12", "Aston Martin", "Db series",'46r6grt6','240000',"248000")



