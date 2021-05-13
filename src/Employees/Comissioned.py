import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Employees.Employee import Employee

class Comissioned(Employee):
    def __init__(self, name, rg, id, adress, wage):
        super().__init__(name, rg, id, adress)
        self.__wage = wage
        self.__comission = 0

    def get_wage(self):
        return self.__wage
    def set_wage(self, wage):
        self.__wage = wage

    def get_comission(self):
        return self.__comission
    
    def add_comission(self, comission):
        self.__comission += comission

    def clear_comission(self):
        self.__comission = 0