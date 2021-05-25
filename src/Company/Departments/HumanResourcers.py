import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from RegisterTools.EmployeesRegister import EmployeesRegister
from RegisterTools.TimeRegister import TimeRegister

REGISTER = EmployeesRegister()
class HumanResourcers():
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
        return REGISTER.add_employee(emp_type, name, rg, adress, hour_value, wage)

    def remove_employee_hr(self, emp_id):
        REGISTER.remove_employee(emp_id)

    def change_employee_details(self, emp_id, emp_t=None, name=None, rg=None, adress=None, hour_value=None, wage=None):
        emp = REGISTER.change_employee_details(emp_id, emp_t, name, rg, adress, hour_value, wage)
        print("\n\nAlteracao bem sucedida!")
        self.show_full_employee_details(emp_id=emp.id)

    def show_full_employee_details(self, emp_id):
        i = REGISTER.employee_finder(emp_id)
        if i:
            emp = REGISTER.employees_list[i]
            print("\n\nID:",emp.id,"\nTipo de Empregado:",emp.__class__.__name__, "\nNome:", emp.name,"\nRG:", emp.rg,"\nEndereco", emp.adress, "\n\n")
