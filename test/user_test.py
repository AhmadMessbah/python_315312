from model.entity.user import User
from model.service.employee_service import UserService
from datetime import date

b_d = date(2000,11,10)
user = User( 1, "alireza", "alipour", b_d, "ali", "ali12345", False)

UserService.edit(user)