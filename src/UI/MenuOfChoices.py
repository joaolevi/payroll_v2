class MenuOfChoices():
    def __init__(self):
        self.escolha = -1
    
    def main_menu(self):
        print("Escolha uma opção: ")
        print("0 - Exibir detalhes do empregado\n1 - Adicionar empregado\n2 - Remover empregado\n3 - Lançar um Cartão de Ponto\n4 - Lançar um Resultado Venda\n5 - Lançar uma taxa de serviço\n6 - Alterar detalhes de um empregado\n7 - Rodar a folha de pagamento para hoje\n8 - Agenda de Pagamento\n9 - Criação de Novas Agendas de Pagamento\n\n10 - Sair\n\n")
        self.escolha = int(input("Opcao: "))
        return self.escolha

    def menu_employee_types(self):
        print("Tipo de empregado: \n")
        print("1 - Comissionado\n2 - Horista\n3 - Salariado")
        self.escolha = int(input("Digite a opção: "))
        if self.escolha == 1: return "Comissioned"
        elif self.escolha == 2: return "Hourly"
        else: return "Salaried"

    def menu_payment_types(self):
        print("Metodo de pagamento: \n")
        print("1 - Crédito em Conta\n2 - Cheque em mãos\n3 - Cheque via correios\n")
        self.escolha = int(input("Metodo escolhido: "))
        if self.escolha == 1: return "AccountCredit"
        elif self.escolha == 2: return "CheckOnHands"
        else: return "DeliveryCheck"

    def menu_change_emp_details(self):
        print("Escolha o atributo que deseja alterar: ")
        print("1 - Tipo de empregado\n2 - Nome\n3 - RG\n4 - Endereço\n5 - Dados Bancários\n6 - Método de pagamento\n7 - Salário\n8 - Valor da hora de trabalho\n\n9 - Alterar\n10 - Sair sem alterar")
        self.escolha = int(input("Escolha: "))
        return self.escolha

    def fill_in_bank_data(self):
        bankID = input("Banco: ")
        agency = input("Agencia: ")
        account = input("Conta: ")
        return bankID, agency, account

    def fill_in_date_format(self):
        print("Data: ")
        day = input("Dia: ")
        mounth = input("Mes: ")
        year = input("Ano: ")
        return year+"-"+mounth+"-"+day 