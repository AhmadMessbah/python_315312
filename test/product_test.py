from model.entity.product import Product


product_test = Product( 1234567, "DB12", "Aston Martin", "DB series","2dk4576vh","24000","248000")
print(product_test)
print(product_test.to_tuple())
