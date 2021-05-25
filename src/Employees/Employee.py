class Employee:
    def __init__(self, name, rg, id, adress):
        self.name = name
        self.rg = rg
        self.adress = adress
        self.id = id

    def get_name(self): return self.name
    def set_name(self, name):
        self.name = name

    def get_adress(self): return self.adress
    def set_adress(self, new_adress): self.adress = new_adress

    def get_rg(self):
        return self.rg
    def set_rg(self, new_rg):
        self.rg = new_rg

    def get_id(self):
        return self.id
    def set_id(self, new_id):
        self.id = new_id

    def __repr__(self):
        return "Nome: %s ID: %s" %(self.name, self.id)