class BankData():
    def __init__(self, bankID, agency, account):
        self.bankID = bankID
        self.agency = agency
        self.account = account
    
    def get_bankID(self):
        return self.bankID
    def set_bankID(self, new_bankID):
        self.bankID = new_bankID
    
    def get_agency(self):
        return self.agency
    def set_agency(self, new_agency):
        self.agency = new_agency
    
    def get_account(self):
        return self.account
    def set_account(self, new_account):
        self.account = new_account

    def __repr__(self):
        return "bankID: %s, agency: %s, account: %s\n" %(self.bankID, self.agency, self.account)