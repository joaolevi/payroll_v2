from .PayMethod import PayMethod
from ..BankData import BankData

class CheckOnHands(BankData, PayMethod):
    def __init__(self, value, date, bankID, agency, account, check_num):
        PayMethod.__init__(self, value, date)
        BankData.__init__(self, bankID, agency, account)
        self.checkNum: check_num

    def get_checkNum(self):
        return self.checkNum
    def set_checkNum(self, new_checkNum):
        self.checkNum = new_checkNum