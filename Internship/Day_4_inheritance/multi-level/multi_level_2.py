class grand_father:
    def __init__(self, g_property):
        self.grand_father_property = g_property

    def display_property1(self):
        print("The grand father property is", self.grand_father_property)


class father(grand_father):
    def __init__(self, f_property, g_property):
        super().__init__(g_property)
        self.father_property = f_property

    def display_property2(self):
        print("The father property is", self.father_property)


class son(father):
    def __init__(self, s_property, f_property, g_property):
        super().__init__(f_property, g_property)
        self.son_property = s_property

    def display_property3(self):
        print("The son property is", self.son_property)



son_obj = son("Bike", "Car", "House")
g_f= grand_father("bullet")
g_f.display_property1()
son_obj.display_property1()
son_obj.display_property2()
son_obj.display_property3()
