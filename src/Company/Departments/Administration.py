from ..Company import Company

class Administration(Company):
    def __init__(self):
        self.__paySchedules = []
        self.__employeesPayDate = []

    def get_paySchedules(self):
        return self.__paySchedules
    def set_paySchedules(self, new_paySchedules):
        self.__paySchedules = new_paySchedules

    def get_employeesPayDate(self):
        return self.__employeesPayDate

    def getOnlyOneEmpPayDate(self, emp_id):
        for employee in self.__employeesPayDate:
            if employee['id'] == emp_id:
                return employee['date']

    def setOnlyOneEmpPayDate(self, emp_id, new_payDate):
        for employee in self.__employeesPayDate:
            if employee['id'] == emp_id:
                employee['date'] = new_payDate
        