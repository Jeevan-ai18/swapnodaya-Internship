class Person:
    def __init__(self, name):
        self.name = name
    def display_person(self):
        print(self.name)

class Student(Person):
    def __init__(self,student_id,name):
        Person.__init__(self,name)
        self.student_id = student_id

    def display_student(self):
        print(self.student_id)

class SportsPlayer(Person):
    def __init__(self,sport_name,name):
       Person.__init__(self,name)
       self.sport_name = sport_name
    def display_sports_player(self):
        print(self.sport_name)

class CollegeStudent(Student, SportsPlayer):
    def __init__(self,college_name,student_id,sports_name,name):
        SportsPlayer.__init__(self,sports_name,name)
        Student.__init__(self,student_id,name)
        self.college_name = college_name
    def display_college(self):
        print(self.college_name)

Final=CollegeStudent("mandavya","   22ISE","Basketball","rakesh")
Final.display_person()
Final.display_student()
Final.display_sports_player()
Final.display_college()
