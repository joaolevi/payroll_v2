from .CheckOnHands import CheckOnHands

class DeliveryCheck(CheckOnHands):
    def __init__(self, value, date, bankID, companyAgency, companyAccount, check_num, adress):
        super().__init__(value, date, bankID, companyAgency, companyAccount, check_num)
        self.adress: adress
    
    def get_adress(self):
        return self.adress
    def set_adress(self, new_adress):
        self.adress = new_adress