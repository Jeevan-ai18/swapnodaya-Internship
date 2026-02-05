#single inheritance
class father:
    def __init__(self,surname,fname):
        self.surname=surname
        self.fname=fname
    def display_surname(self):
        print("surname is ", self.surname)
    def display_father_name(self):
        print("father name is ", self.fname,self.surname)
class son(father):
    def __init__(self,name,surname,fname):
        self.name=name
        super().__init__(surname, fname)
    def display_name(self):
        print("name is ", self.name)
    def display_name2(self):
        print("name is ", self.name,self.surname,self.fname)

s1=son("Jeevan","gowda","mache")
s1.display_name()
s1.display_name2()
s1.display_surname()
s1.display_father_name()
