import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from RegisterTools.Sales import Sales
from Company.Company import Company

class Finances(Company):
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
    
    def setSaleToEmployee(self, date, value, emp_id, comission):
        s = Sales(date, value, emp_id, comission)
        self.__paymentRegister.append(s)

    def setTaxToEmployee():
        pass

    def payEmployees():
        pass