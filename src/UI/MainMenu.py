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
from UI.FinancesUI import FinancesUI

MENU_OF_CHOICES = MenuOfChoices()

class MainMenu():
    def __init__(self):
        self.opcao = -1
        self.HumanResourcers = HumanResourcers()
        self.Finances = Finances()
        self.Administration = Administration()

    def menu_initial(self):
        while(self.opcao != 10):
            self.opcao = MENU_OF_CHOICES.main_menu()
            if self.opcao == 0:
                emp_id = input("ID do empregado: ")
                self.HumanResourcers.show_full_employee_details(emp_id)
            elif self.opcao == 1:
                self.HumanResourcers, self.Finances, self.Administration = HumanResourcersUI.add_employee_ui(self.HumanResourcers, self.Finances, self.Administration)
            elif self.opcao == 2:
                self.HumanResourcers, self.Finances, self.Administration = HumanResourcersUI.employee_remove_ui(self.HumanResourcers, self.Finances, self.Administration)
            elif self.opcao == 3:
                self.HumanResourcers = HumanResourcersUI.time_register(self.HumanResourcers)
            elif self.opcao == 4:
                self.Finances = FinancesUI.set_sale_to_emp(self.Finances)
            elif self.opcao == 6:
                self.HumanResourcers, self.Finances = HumanResourcersUI.change_employee_datails_ui(self.HumanResourcers, self.Finances)

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


MainMenu().menu_initial()