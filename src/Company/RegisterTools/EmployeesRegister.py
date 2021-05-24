import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Employees.Salaried import Salaried
from Employees.Hourly import Hourly
from Employees.Comissioned import Comissioned

class EmployeesRegister():
    def __init__(self):
        self.employees_list = []
    
    def get_employees_list(self):
        return self.employees_list
    def clear_employees_list(self):
        self.employees_list = []

    def employee_finder(self, emp_id):
        x = -1
        tam = len(self.employees_list)
        while x < tam:
            if self.employees_list[x].id == emp_id:
                return x
            x+=1
        if x < tam:
            return x

    def add_employee(self, emp_type, name, rg, adress, hour_value=None, wage=None):
        new_id = int(str(rg[:6]))*27
        if emp_type == "Comissioned":
            emp = Comissioned(name=name, rg=rg, id=new_id, adress=adress, wage=wage)
        elif emp_type == "Hourly":
            emp = Hourly(name=name, rg=rg, id=new_id, adress=adress, hourValue=hour_value)
        else:
            emp = Salaried(name=name, rg=rg, id=new_id, adress=adress, wage=wage)
        self.employees_list.append(emp)
        
    
    def remove_employee(self, emp_id):
        i = self.employee_finder(emp_id)
        if i:
            emp = self.employees_list[i]
            self.employees_list.remove(emp)
        
    def change_employee_type(self, emp_id, emp_type, hour_value=None, wage=None):
        i = self.employee_finder(emp_id)
        emp = self.employees_list[i]
        if emp_type:
            self.remove_employee(emp.id)
            self.add_employee(emp_type=emp_type, name=emp.name, rg=emp.rg, adress=emp.adress, hour_value=None, wage=None)
            index = self.employee_finder(emp.id)
            return index
    
    def change_employee_details(self, emp_id, emp_t=None, name=None, rg=None, adress=None, hour_value=None, wage=None):
        i = self.employee_finder(emp_id)
        if emp_t:
            i = self.change_employee_type(emp_id, emp_t, hour_value, wage)
        if name:
            self.employees_list[i].set_name(name)
        if rg:
            self.employees_list[i].set_rg(rg)
        if adress:
            self.employees_list[i].set_adress(adress)
        return self.employees_list[i]