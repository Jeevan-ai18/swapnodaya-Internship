class father:
    def __init__(self,surname,father_name):
        self.surname = surname
        self.father_name = father_name
    def display_suranme(self):
        print(self.surname)

class son(father):
    def __init__(self,name,father_name):
        super().__init__(surname,father_name)
        self.name = name

    def display_son_name(self):


