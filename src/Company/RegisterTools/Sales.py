class Sales:
    def __init__(self, date, value, emp_id, comission):
        self.__date = date
        self.__value = value
        self.__seller = emp_id
        self.__comission = comission
    
    def get_date(self):
        return self.__date
    def set_date(self, new_date):
        self.__date = new_date
    
    def get_value(self):
        return self.__value
    def set_value(self, new_value):
        self.__value = new_value
    
    def get_seller(self):
        return self.__seller
    def set_seller(self, new_seller):
        self.__seller = new_seller
    
    def get_comission(self):
        return self.__comission
    def set_comission(self, new_comission):
        self.__comission = new_comission
    
    def __repr__(self):
        return "%s : %s : %.2f : %.2f\n" %(self.__date, self.__seller, self.__value, self.__comission)