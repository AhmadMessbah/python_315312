import mysql.connector

from model.entity.product import Product


# save, edit, remove, find_all(), find_by_id()
class ProductRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="mft"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, product):
        self.connect()
        self.cursor.execute("insert into product_tbl (id,name,brand,model,barcode,buy_price,sell_price) values (%s,%s,%s,%s,%s,%s,%s)",
                            [product.id, product.name, product.brand, product.model, product.barcode, product.buy_price, product.sell_price])
        self.connection.commit()
        self.disconnect()

    def edit(self, product):
        self.connect()
        self.cursor.execute("update product_tbl set id=%s,name=%s,brand=%s, model=%s, barcode = %s, buy_price=%s,sell_price=%s where id=%s",
                            [product.id,product.name,product.brand,product.model, product.barcode, product.buy_price, product.sell_price])
        self.connection.commit()
        self.disconnect()

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from product_tbl where id=%s", [id])
        self.connection.commit()
        self.disconnect()


    def find_all(self):
        self.connect()
        self.cursor.execute("select * from product_tbl")
        product_list = self.cursor.fetchall()
        product_list = [Product(*pros) for pros in product_list]
        self.disconnect()
        if product_list:
            return product_list


    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from product_tbl where id=%s", [id])
        pro = self.cursor.fetchone()
        self.disconnect()
        if pro:
            pro = Product(*pro)
            return pro
