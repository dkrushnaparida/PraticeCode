class Emp:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getInfo(self):
        print(f"employee name : {self.name},  and address {self.address}")

data = Emp("dwiti", "Odisha")
data.getInfo()