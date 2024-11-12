#Hierarchical Inheritance
class student1:
    def __init__(self):
            print("DYP")
            
class student2():
    def name(self):
        print("Namrata")

class rollno(student1,student2):
    def roll(self):
        print("66")

obj1 = rollno()
obj1.name()
obj1.roll()