import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from MenuOfChoices import MenuOfChoices

MENU_OF_CHOICES = MenuOfChoices()

class HumanResourcersUI():
    def __init__(self):
        pass
    
    def add_employee_ui(HumanResourcers, Finances, Administration):
        wage, hour_value = None, None
        name = input("Nome: ")
        rg = input("Rg: ")
        adress = input("Endereço: ")
        emp_type = MENU_OF_CHOICES.menu_employee_types()
        if emp_type == "Hourly":
            hour_value = float(input("Valor da hora de trabalho: "))
        else: 
            wage = float(input("Salario: "))
        bankID, agency, account = MENU_OF_CHOICES.fill_in_bank_data()
        paymentType = MENU_OF_CHOICES.menu_payment_types()
        emp_id = HumanResourcers.add_employee(emp_type, name, rg, adress, hour_value, wage)
        Administration.add_employeePayDate(emp_id, emp_type)
        Finances.add_employee_finances(emp_id, 0, bankID, agency, account, paymentType)
        HumanResourcers.show_full_employee_details(emp_id)
        return HumanResourcers, Finances, Administration

    def employee_remove_ui(HumanResourcers, Finances, Administration):
        emp_id = int(input("ID do empregado: "))
        HumanResourcers.remove_employee_hr(emp_id)
        Finances.remove_employee_fin(emp_id)
        Administration.remove_employee_adm(emp_id)
        return HumanResourcers, Finances, Administration

    def change_employee_datails_ui(HumanResourcers, Finances):
        escolha = -1
        emp_type, name, adress, rg, bankID, agency, account, paymentMethod, new_wage, hour_value = None, None, None, None, None, None, None, None, None, None
        emp_id = int(input("ID do empregado: "))
        while (escolha != 10):
            escolha = MENU_OF_CHOICES.menu_change_emp_details()
            if escolha == 1:
                emp_type = MENU_OF_CHOICES.menu_employee_types()
            elif escolha == 2:
                name = str(input("Nome: "))
            elif escolha == 3:
                rg = input("RG: ")
            elif escolha == 4:
                adress = input("Endereco: ")
            elif escolha == 5:
                bankID, agency, account = MENU_OF_CHOICES.fill_in_bank_data()
            elif escolha == 6:
                paymentMethod = MENU_OF_CHOICES.menu_payment_types()
            elif escolha == 7:
                new_wage = float(input("Novo salario: "))
            elif escolha == 8:
                hour_value = float(input("Valor da Hora de trabalho: "))
            elif escolha == 9:
                HumanResourcers.change_employee_details(emp_id, emp_type, name, rg, adress, hour_value, new_wage)
                Finances.change_emp_fin_data(emp_id, bankID, agency, account, paymentMethod)
                return HumanResourcers, Finances
            else: return

    def time_register(HumanResourcers):
        emp_id = int(input("ID do empregado: "))
        date = MENU_OF_CHOICES.fill_in_date_format()
        worked_hours = float(input("Horas trabalhadas: "))
        HumanResourcers.set_employeeTimeRegister(emp_id, date, worked_hours)
        return HumanResourcers
