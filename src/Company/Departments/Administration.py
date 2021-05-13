from ..Company import Company

class Administration(Company):
    def __init__(self):
        self.__paySchedules = []
        self.__empPayDate = []

    def get_paySchedules(self):
        return self.__paySchedules
    def set_paySchedules(self, new_paySchedules):
        self.__paySchedules = new_paySchedules

    def get_empPayDate(self):
        return self.__empPayDate
    #It sill need more dev
    def set_empPayDate(self, new_payDate):
        pass

    def createNewSchedule():
        pass

    def setOnlyOneEmpPayDate():
        pass