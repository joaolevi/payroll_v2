import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Employees.Employee import Employee

class Salaried(Employee):
    def __init__(self, name, rg, id, adress, wage):
        super().__init__(name, rg, id, adress)
        self.wage = wage

    def get_wage(self):
        return self.wage
    def set_wage(self, value):
        self.wage = value