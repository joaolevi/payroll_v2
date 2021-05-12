class PayMethod():
    def __init__(self, value, date):
        self.__value = value
        self.__date = date

    def get_value(self):
        return self.__value
    def set_value(self, new_value):
        self.__value = new_value
    
    def get_date(self):
        return self.__date
    def set_date(self, new_date):
        self.__date = new_date