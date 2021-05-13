from .Employee import Employee

class Hourly(Employee):
    def __init__(self, name, rg, id, adress, hourValue):
        super().__init__(name, rg, id, adress)
        self.hourValue = hourValue

    def get_hourValue(self):
        return self.hourValue
    def set_hourValue(self, value):
        self.hourValue = value