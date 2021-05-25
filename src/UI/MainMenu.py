import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# from Company import Company
from Company.Departments.HumanResourcers import HumanResourcers
from Company.Departments.Finances import Finances
from Company.Departments.Administration import Administration
from UI.MenuOfChoices import MenuOfChoices
from UI.HumanResourcersUI import HumanResourcersUI

MENU_OF_CHOICES = MenuOfChoices()

class MainMenu():
    def __init__(self):
        self.opcao = -1
        self.HumanResourcers = HumanResourcers()
        self.Finances = Finances()
        self.Administration = Administration()

    def menu_initial(self):
        self.opcao = MENU_OF_CHOICES.main_menu()
        if self.opcao == 1:
            self.add_employee()

    def emp_details(self):
        emp_id = input("ID do empregado: ")
        self.HumanResourcers.show_full_employee_details(emp_id)

    def add_employee(self):
        self.Administration, self.Finances, self.HumanResourcers = HumanResourcersUI.add_employee_ui(self.HumanResourcers, self.Finances, self.Administration)
    
    # def add_employee(self):
    #     wage, hour_value = None, None
    #     name = input("Nome: ")
    #     rg = input("Rg: ")
    #     adress = input("Endereço: ")
    #     emp_type = MENU_OF_CHOICES.menu_employee_types()
    #     if emp_type == "Hourly":
    #         hour_value = float(input("Valor da hora de trabalho: "))
    #     else: 
    #         wage = float(input("Salario: "))
    #     bankID, agency, account = MENU_OF_CHOICES.fill_in_bank_data()
    #     paymentType = MENU_OF_CHOICES.menu_payment_types()
    #     emp_id = self.HumanResourcers.add_employee(emp_type, name, rg, adress, hour_value, wage)
    #     self.Administration.add_employeePayDate(emp_id, emp_type)
    #     self.Finances.add_employee_finances(emp_id, 0, bankID, agency, account, paymentType)
    #     self.HumanResourcers.show_full_employee_details(emp_id)

    def employee_remove(self):
        self.HumanResourcers, self.Finances, self.Administration = HumanResourcersUI.employee_remove(self.HumanResourcers, self.Finances, self.Administration)

    def set_time_register(self):
        emp_id = int(input("ID do empregado: "))
        date = MENU_OF_CHOICES.fill_in_date_format()
        worked_hours = float(input("Horas trabalhadas: "))
        self.HumanResourcers.set_employeeTimeRegister(emp_id, date, worked_hours)

    def set_sale_to_emp(self):
        emp_id = int(input("ID do empregado: "))
        date = MENU_OF_CHOICES.fill_in_date_format()
        value = float(input("Valor da venda: "))
        comission = float(input("Comissao em %: "))
        comission = value*comission/100
        self.Finances.setSaleToEmployee(date, value, emp_id, comission)

    def set_tax_to_emp(self):
        emp_id = int(input("ID do empregado: "))
        tax_value = float(input("Valor da taxa: "))
        self.Finances.setTaxToEmployee(emp_id, tax_value)

    def change_emp_details(self):
        pass


MainMenu().menu_initial()
MainMenu().employee_remove()