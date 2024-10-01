from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.entity.base import Base
from model.entity.book import Book
from model.entity.employee import Employee

# connection   -> engine
# cursor(sql)  -> session

url = "mysql+pymysql://root:root123@localhost/mft"

if not database_exists(url):
    create_database(url)

engine = create_engine(url)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

class CrudRepository:
    def __init__(self, class_name):
        self.class_name = class_name


    def save(self,entity):
        session = Session()
        session.add(entity)
        session.commit()
        session.refresh(entity)
        # session.close()
        return entity


    def edit(self,entity):
        session = Session()
        entity = session.get(self.class_name,entity._id)
        session.merge(entity)
        session.commit()
        session.refresh(entity)
        # session.close()
        return entity


    # def remove(self, id):
    #     self.connect()
    #     self.cursor.execute("delete from employee_tbl where id=%s", [id])
    #     self.connection.commit()
    #     self.disconnect()
    #
    #
    def find_all(self):
        session = Session()
        return session.query(self.class_name).all()


    def find_by_id(self, id):
        session = Session()
        return session.get(self.class_name, id)

    def find_by(self, find_term):
        session = Session()
        return session.query(self.class_name)

emp = Employee(None, "ali", "alipour", 20)

repo = CrudRepository(Employee)
repo.save(emp)

print(emp)


# book = Book(15, "Java", "MFT", 800)
# print(book)
# repo = CrudRepository(Book)
# repo.save(book)
# print(book)
# print(repo.edit(book))

# print(repo.find_by(Book.title == "Java"))
# print(repo.find_by(Employee.name == "ali"))