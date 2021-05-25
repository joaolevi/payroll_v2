class Administration():
    def __init__(self):
        self.__paySchedules = ["weekly-1-friday", "weekly-2-friday", "mounth-$"]
        self.__employeesPayDate = []

    # Métodos de acesso

    def get_paySchedules(self):
        return self.__paySchedules
    def set_paySchedules(self, new_paySchedules):
        self.__paySchedules = new_paySchedules
        print(new_paySchedules)

    def get_employeesPayDate(self):
        return self.__employeesPayDate

    # Funções específicas

    def add_employeePayDate(self, emp_id, emp_type):
        if emp_type == "Hourly":
            self.__employeesPayDate.append({'id':emp_id, 'date':'weekly-1-friday'})
        elif emp_type == "Comissioned":
            self.__employeesPayDate.append({'id':emp_id, 'date':'weekly-2-friday'})
        else: self.__employeesPayDate.append({'id':emp_id, 'date':'mounth-$'})
    
    def remove_employee_adm(self, emp_id):
        for e in self.__employeesPayDate:
            if e['id'] == emp_id:
                self.__employeesPayDate.remove(e)

    def getOnlyOneEmpPayDate(self, emp_id):
        for employee in self.__employeesPayDate:
            if employee['id'] == emp_id:
                return employee['date']

    def setOnlyOneEmpPayDate(self, emp_id, new_payDate):
        for employee in self.__employeesPayDate:
            if employee['id'] == emp_id:
                employee['date'] = new_payDate
                print(employee)
        