import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Company import Company
from RegisterTools.EmployeesRegister import EmployeesRegister
from RegisterTools.TimeRegister import TimeRegister

REGISTER = EmployeesRegister()
class HumanResourcers(Company):
    def __init__(self):
        self.employeeTimeRegister = []
    
    def get_employeeTimeRegister(self):
        return self.employeeTimeRegister
    def set_employeeTimeRegister(self, emp_id, date, workedHours):
        tr = TimeRegister(emp_id, date, workedHours)
        self.employeeTimeRegister.append(tr)

    def show_employees(self):
        print(REGISTER.get_employees_list())
    
    def add_employee(self, emp_type, name, rg, adress, hour_value=None, wage=None):
        REGISTER.add_employee(emp_type, name, rg, adress, hour_value, wage)

    def remove_employee(self, emp_id):
        REGISTER.remove_employee(emp_id)

    def change_employee_details(self, emp_id, emp_t=None, name=None, rg=None, adress=None, hour_value=None, wage=None):
        emp = REGISTER.change_employee_details(emp_id, emp_t, name, rg, adress)
        print("\n\nAlteracao bem sucedida!")
        self.show_full_employee_details(emp_id=emp.id)

    def show_full_employee_details(self, emp_id):
        i = REGISTER.employee_finder(emp_id)
        if i:
            emp = REGISTER.employees_list[i]
            print("\n\nID:",emp.id,"\nTipo de Empregado:",emp.__class__.__name__, "\nNome:", emp.name,"\nRG:", emp.rg,"\nEndereco", emp.adress, "\n\n")

# RH = HumanResourcers()

# RH.add_employee("Comissioned", "Joao", "12312", "Rua Helena", wage=12345)
# # RH.show_employees()
# # RH.show_full_employee_details(332424)

# # RH.change_employee_details(332424, name="Levizinho do arrcha", adress="Endereco 2")
# RH.change_employee_details(332424, emp_t="Hourly", hour_value=1251, rg=121242)
