class EmployeesPayCheck():
    def __init__(self):
        self.employees_paycheck = []
    
    def get_employees_paycheck(self):
        return self.employee_paycheck
    def clear_employees_paycheck(self):
        self.employees_paycheck = []

    def add_employee_payCheck(self, pc):
        self.employees_paycheck.append(pc)
    
    def getOnlyEmpPayCheckIndex(self, emp_id):
        i = 0
        for e in self.employees_paycheck:
            if e.id == emp_id:
                return i
            i += 1
        return False

    def getOnlyEmpPayCheck(self, emp_id):
        for e in self.employees_paycheck:
            if e.id == emp_id:
                return e

