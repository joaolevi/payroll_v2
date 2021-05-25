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
        return Administration, Finances, HumanResourcers

    def employee_remove(HumanResourcers, Finances, Administration):
        emp_id = int(input("ID do empregado: "))
        HumanResourcers.remove_employee_hr(emp_id)
        Finances.remove_employee_fin(emp_id)
        Administration.remove_employee_adm(emp_id)
        return HumanResourcers, Finances, Administration