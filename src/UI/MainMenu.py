import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# from Company import Company
from Company.Departments.HumanResourcers import HumanResourcers
from Company.Departments.Finances import Finances
from Company.Departments.Administration import Administration
from UI.MenuOfChoices import MenuOfChoices
from UI.DepartamentsUI.HumanResourcersUI import HumanResourcersUI
from UI.DepartamentsUI.FinancesUI import FinancesUI
from UI.DepartamentsUI.AdministrationUI import AdministrationUI

MENU_OF_CHOICES = MenuOfChoices()

class MainMenu():
    def __init__(self):
        self.opcao = -1
        self.HumanResourcers = HumanResourcers()
        self.Finances = Finances()
        self.Administration = Administration()

    def menu_admin(self):
        print("\n1 - Alterar data de pagamento de um empregado\n2 - Exibir agenda de pagamento\n3 - Criar nova agenda de pagamento\n\n4 - Voltar\n\n")
        op = int(input("Digite o numero da opcao desejada: "))
        if op == 1:
            self.Administration = AdministrationUI.change_emp_paydate(self.Administration)
        elif op == 2:
            print(self.Administration.get_paySchedules())
        elif op == 3:
            self.Administration = AdministrationUI.create_new_schedule(self.Administration)
        else: return
    
    def menu_hr(self):
        print("\n1 - Exibir detalhes do empregado\n2 - Adicionar empregado\n3 - Remover empregado\n4 - Alterar detalhes do empregado\n5 - Registrar Ponto do Empregado\n6 - Exibir lista de empregados\n\n7 - Voltar\n\n")
        op = int(input("Digite a opcao desejada: "))
        if op == 1:
            emp_id = input("ID do empregado: ")
            self.HumanResourcers.show_full_employee_details(emp_id)
        elif op == 2:
            self.HumanResourcers, self.Finances, self.Administration = HumanResourcersUI.add_employee_ui(self.HumanResourcers, self.Finances, self.Administration)
        elif op == 3:
            self.HumanResourcers, self.Finances, self.Administration = HumanResourcersUI.employee_remove_ui(self.HumanResourcers, self.Finances, self.Administration)
        elif op == 4:
            self.HumanResourcers, self.Finances = HumanResourcersUI.change_employee_datails_ui(self.HumanResourcers, self.Finances)
        elif op == 5:
            self.HumanResourcers = HumanResourcersUI.time_register(self.HumanResourcers)
        elif op == 6:
            self.HumanResourcers.show_employees()
        else: return

    def menu_fin(self):
        print("\n1 - Lancar Resultado de Venda\n2 - Lancar uma taxa de servico\n3 - Exibir dados financeiros de um empregado\n4 - Exibir registro de vendas\n5 - Exibir pagamentos\n\n6 - Voltar")
        op = int(input("Digite a opcao desejada: "))
        if op == 1:
            self.Finances = FinancesUI.set_sale_to_emp(self.Finances)
        elif op == 2:
            self.Finances = FinancesUI.set_tax_to_emp(self.Finances)
        elif op == 3:
            emp_id = int(input("ID do empregado: "))
            self.Finances.show_emp_details(emp_id)
        elif op == 4:
            print(self.Finances.get_sales())
        elif op == 5:
            print(self.Finances.get_paymentRegister())
        else: return

    def menu_initial(self):
        while(self.opcao != 4):
            print("Menu da Compania\n\n1 - Administrativo\n2 - Recursos Humanos\n3 - Financeiro\n\n4 - Sair\n\n")
            self.opcao = int(input("Digite a opcao desejada: "))
            if self.opcao == 1:
                self.menu_admin()
            elif self.opcao == 2:
                self.menu_hr()
            elif self.opcao == 3:
                self.menu_fin()
            else: return


MainMenu().menu_initial()