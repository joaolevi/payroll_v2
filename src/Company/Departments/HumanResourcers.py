from ..Company import Company
from ..RegisterTools.EmployeesRegister import EmployeesRegister
from ..RegisterTools.TimeRegister import TimeRegister

REGISTER = EmployeesRegister()
class HumanResourcers(Company):
    def __init__(self):
        self.employeeTimeRegister = []
    
    def get_employeeTimeRegister(self):
        return self.employeeTimeRegister
    def set_employeeTimeRegister(self, emp_id, date, workedHours):
        tr = TimeRegister(emp_id, date, workedHours)
        self.employeeTimeRegister.append(tr)
    
    def add_employee(self, emp_type, name, rg, adress, hour_value=None, wage=None):
        REGISTER.add_employee(emp_type, name, rg, adress, hour_value, wage)

    def remove_employee(self, emp_id):
        REGISTER.remove_employee(emp_id)

    def change_employee_details(self, emp_id, emp_t=None, name=None, rg=None, adress=None, bankAcc=None, payMethod=None, wage=None):
        pass