from model.entity.user import User
from model.service.employee_service import UserService
from datetime import date

b_d = date(2000,11,10)
user1 = User(1, "alireza", "alipour", b_d, "ali", "ali12345", False)
print(user1)
print(user1.to_tuple())

user_service = UserService()

user_service.save(user1)
UserService.edit(user1)
UserService.delete()

print(user_service.find_by_id(1))
print(user_service.find_all())


print(User.Controller.save(2,"reza","rezapour",b_d ,"reza","reza12345", True))
