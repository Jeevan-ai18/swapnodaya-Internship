class product:
    def __init__(self,productname,price):
        self.productname = productname
        self.price = price
    def display(self):
        print(self.productname,self.price)

class Electronicproduct(product):
    def __init__(self,brand,warranty,productname,price):
        self.brand = brand
        self.warranty = warranty
        super().__init__(productname,price)

class MobilePhone(Electronicproduct):
    def __init__(self,ram,storage,brand,warranty,productname,price):
        self.ram = ram
        self.storage = storage
        super().__init__(brand,warranty,productname,price)

    def display_mobile_details(self):
        print("Ram",self.ram,"Storage",self.storage)
        print("Productname",self.productname,"price", self.price)
        print("Brand",self.brand,"warrenty",self.warranty)

Mobil=MobilePhone("12gb","125gb","samsong",
                  "2years","samsong_galaxy_s24","150000")
Mobil.display_mobile_details()