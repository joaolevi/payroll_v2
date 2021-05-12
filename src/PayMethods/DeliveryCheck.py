import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from PayMethods.CheckOnHands import CheckOnHands

class DeliveryCheck(CheckOnHands):
    def __init__(self, value, date, bankID, companyAgency, companyAccount, check_num, adress):
        super().__init__(value, date, bankID, companyAgency, companyAccount, check_num)
        self.adress: None
    
    def get_adress(self):
        return self.adress
    def set_adress(self, new_adress):
        self.adress = new_adress