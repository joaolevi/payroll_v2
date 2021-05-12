class TimeRegister:
    def __init__(self, date, hours):
        self.date = date
        self.hours = hours

    def get_date(self):
        return self.__date
    def set_date(self, new_date):
        self.__date = new_date
    
    def get_hours(self):
        return self.__hours
    def set_hours(self, new_hours):
        self.__hours = new_hours
    
    def __repr__(self):
        return "%s -- %s\n" %(self.__date, self.__hours)