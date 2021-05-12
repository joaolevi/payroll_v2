import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from PayMethods.PayMethod import PayMethod
from BankDatas.BankData import BankData

class CheckOnHands(BankData, PayMethod):
    def __init__(self, value, date, bankID, agency, account, check_num):
        PayMethod.__init__(self, value, date)
        BankData.__init__(self, bankID, agency, account)
        self.checkNum: check_num

    def get_checkNum(self):
        return self.checkNum
    def set_checkNum(self, new_checkNum):
        self.checkNum = new_checkNum