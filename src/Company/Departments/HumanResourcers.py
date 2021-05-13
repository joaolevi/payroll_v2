from ..Company import Company

class HumanResourcers(Company):
    def __init__(self):
        self.employee_list = []
        self.employeeTimeRegister = []
    
    def get_employee_list(self):
        return self.employee_list
    def set_employee_list(self, new_list):
        self.employee_list = new_list
    
    def get_employeeTimeRegister(self):
        return self.employeeTimeRegister
    def set_employeeTimeRegister(self, new_timeList):
        self.employeeTimeRegister = new_timeList
    
    def add_employee():
        pass

    def remove_employee():
        pass

    def set_employeeDetails():
        pass

    def employeeFinder():
        pass