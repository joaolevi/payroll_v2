import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from RegisterTools.Sales import Sales
from RegisterTools.EmployeesPayCheck import EmployeesPayCheck
from RegisterTools.EmployeeBankData import EmployeeBankData

REGISTER = EmployeesPayCheck()

class Finances():
    def __init__(self):
        self.__sales = []
        self.__paymentRegister = []

    def get_sales(self):
        return self.__sales
    def set_sales(self, new_list):
        self.__sales = new_list
    
    def get_paymentRegister(self):
        return self.__paymentRegister
    def set_paymentRegister(self, new_payList):
        self.__paymentRegister = new_payList
    
    def add_employee_finances(self, emp_id, value_to_receive, bankID, agency, account, paymentMethod):
        e = EmployeeBankData(emp_id, value_to_receive, bankID, agency, account, paymentMethod)
        REGISTER.add_employee_payCheck(e)
    
    def remove_employee_fin(self, emp_id):
        REGISTER.remove_emp(emp_id)
    
    def setSaleToEmployee(self, date, value, emp_id, comission):
        s = Sales(date, value, emp_id, comission)
        self.__sales.append(s)

    def setTaxToEmployee(self, emp_id, tax_value):
        i = REGISTER.getOnlyEmpPayCheckIndex(emp_id)
        if i >= 0:
            REGISTER.employees_paycheck[i].add_tax_to_discount(tax_value)

    def payEmployees():
        pass

# F = Finances()
# F.add_employee(23412, 1232, 123,1234,12345)
# F.setSaleToEmployee("2021-01-05", 123.2, 23412, 12)
# # print(F.get_sales())
# F.setTaxToEmployee(23412, 231.42)
# print(REGISTER.getOnlyEmpPayCheck(23412))