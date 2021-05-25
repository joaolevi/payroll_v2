import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from BankData import BankData

class EmployeeBankData(BankData):
    def __init__(self, emp_id, value_to_receive, bankID, agency, account, paymentMethod):
        super().__init__(bankID, agency, account)
        self.id = emp_id
        self.value_to_receive = value_to_receive
        self.tax_to_discount = 0
        self.paymentMethod = paymentMethod

    def get_emp_id(self):
        return self.id
    def set_emp_id(self, new_id):
        self.id = new_id
    
    def get_value_to_receive(self):
        return self.value_to_receive
    def set_value_to_receive(self, new_value):
        self.value_to_receive = new_value
    
    def get_tax_to_discount(self):
        return self.tax_to_discount
    def set_tax_to_discount(self, new_tax):
        self.tax_to_discount = new_tax

    def add_tax_to_discount(self, tax):
        self.tax_to_discount += tax

    def clear_employee_tax(self, emp):
        emp.tax_to_discount = 0
        
    def __repr__(self) -> str:
        return "ID: %i, Valor a receber(s/ descontos): %.2f, Descontos: %.2f" %(self.id, self.value_to_receive, self.tax_to_discount)
