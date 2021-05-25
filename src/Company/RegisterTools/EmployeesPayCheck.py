class EmployeesPayCheck():
    def __init__(self):
        self.employees_paycheck = []
    
    def get_employees_paycheck(self):
        return self.employee_paycheck
    def clear_employees_paycheck(self):
        self.employees_paycheck = []

    def add_employee_payCheck(self, pc):
        self.employees_paycheck.append(pc)
    
    def remove_emp(self, emp_id):
        i = self.getOnlyEmpPayCheck(emp_id)
        self.employees_paycheck.remove(i)

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

    def change_emp_data(self, emp_id, bankID, agency, account, paymentMethod):
        i = self.getOnlyEmpPayCheckIndex(emp_id)
        if bankID:
            self.employees_paycheck[i].bankID = bankID
        if agency:
            self.employees_paycheck[i].agency = agency
        if account:
            self.employees_paycheck[i].account = account
        if paymentMethod:
            self.employees_paycheck[i].paymentMethod = paymentMethod
        return self.employees_paycheck[i]


