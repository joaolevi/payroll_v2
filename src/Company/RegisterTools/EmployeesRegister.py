from src.Employees.Salaried import Salaried
from src.Employees.Hourly import Hourly
from src.Employees.Comissioned import Comissioned
from src.Employees import Employee
from ...Employees import *

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
            if self.employeesList[x].id == emp_id:
                return x
            else:
                x+=1
        if x < tam:
            return x

    def add_employee(self, emp_type, name, rg, adress, hour_value=None, wage=None):
        new_id = int(str(rg[:6]))*27
        if emp_type == "Comissioned":
            emp = Comissioned(emp_type, name, rg, adress, wage, id=new_id)
        elif emp_type == "Hourly":
            emp = Hourly(emp_type, name, rg, adress, hour_value, id=new_id)
        else:
            emp = Salaried(emp_type, name, rg, adress, wage, id=new_id)
        self.employees_list.append(emp)
        
    
    def remove_employee(self, emp_id):
        i = self.employee_finder(emp_id)
        if i:
            emp = self.employees_list[i]
            self.employees_list.remove(emp)
        
    def change_employee_type(self, emp_id, emp_type, wage=None):
        i = self.get_employee(emp_id)
        emp = self.employeesList[i]
        if emp_type:
            self.remove_employee(emp.id)
            self.add_employee(name=emp.name, rg=emp.rg, adress=emp.adress, sindMember=emp.sindMember, emp_type=emp_type, wage=wage, payMethod=emp.paymentMethod, date=emp.last_pay_date)
            index = self.get_employee(emp.id)
            return index
    
    def change_employee_details(self, emp_id, emp_t=None, name=None, rg=None, adress=None, bankAcc=None, payMethod=None, wage=None):
        i = self.employee_finder(emp_id)
        if emp_t:
            i = self.change_employee_type(emp_id, emp_t, wage)
        if name:
            self.employeesList[i].set_name(name)
        if rg:
            self.employeesList[i].set_rg(rg)
        if adress:
            self.employeesList[i].set_adress(adress)
        if bankAcc:
            self.employeesList[i].set_bankAcc(bankAcc)
        if payMethod:
            self.employeesList[i].set_paymentMethod(payMethod)
        if wage and (isinstance(self.employeesList[i], Comissioned) or isinstance(self.employeesList[i], Salaried)):
            self.employeesList[i].set_wage(wage)