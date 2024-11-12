#Single Inheritance
class college:
    def __init__(self):
            print("DYP")
            
class student(college):
    def name(self):
        print("Namrata")

obj = student()
obj.name()
        