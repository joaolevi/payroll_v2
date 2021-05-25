class AdministrationUI():
    def __init__(self):
        self.schedule = None

    def change_emp_paydate(Administration):
        emp_id = int(input("ID do empregado: "))
        i = 1
        prazo = Administration.get_paySchedules()
        for p in prazo:
            print(i, "- ", p, "\n")
            i += 1
        t = int(input("Opcao: "))
        Administration.setOnlyOneEmpPayDate(emp_id, prazo[t-1])
        return Administration
    
    def fill_in_paydate_format():
        t = int(input("1 - weekly-1\n2 - weekly-2\n3 - Monthly\n0 - Sair\n"))
        prazo = ["weekly-1", "weekly-2", "monthly"]
        print("Digite o dia\n")
        if t == 3:
            print("Caso seja o ultimo dia util do mes, digite '$'\n")
        day = input("Dia: ")
        return prazo[t-1]+"-"+day

    def create_new_schedule(Administration):
        new_schedule = []
        tam = int(input("Quantas datas deseja criar? "))
        for i in range(tam):
            new_schedule.append(AdministrationUI.fill_in_paydate_format())
        Administration.set_paySchedules(new_schedule)
        return Administration
