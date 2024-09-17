from model.entity.employee import Employee
from model.repository.employee_repository import EmployeeRepository
from model.service.employee_service import EmployeeService
from controller.employee_controller import EmployeeController


controller = EmployeeController()
print(controller.save("ffff", "ggggg", 26))

# emp1 = Employee(2, "aaaa", "bbbb", 27)
#
# emp_service = EmployeeService()
# emp_service.save(emp1)

#
# em_repo = EmployeeRepository()
# em_repo.save(emp1)
# em_repo.edit(emp1)
# em_repo.remove(2)
# print(em_repo.find_all())
# print(em_repo.find_by_id(100))