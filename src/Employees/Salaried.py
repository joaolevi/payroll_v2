from Employees.Employee import Employee

class Salaried(Employee):
    def __init__(self, name, rg, id, adress, wage):
        super().__init__(name, rg, id, adress)
        self.wage = wage

    def get_wage(self):
        return self.wage
    def set_wage(self, value):
        self.wage = value