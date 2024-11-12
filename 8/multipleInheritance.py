#Multiple Inheritance
class college:
    def __init__(self):
            print("DYP")
            
class student1(college):
    def name(self):
        print("Namrata")

class student2(college):
    def roll(self):
        print("66")

obj1 = student1()
obj1.name()
obj2 = student2()
obj2.roll()