#Multilevel Inheritance
class college:
    def __init__(self):
            print("DYP")
            
class student(college):
    def name(self):
        print("Namrata")

class rollno(student):
    def roll(self):
        print("66")

obj = rollno()
obj.roll()
obj.name()