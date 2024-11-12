class myname:

    # default constructor
    def __init__(self):
        self.name = "DYPCET"

    # a method for printing data members
    def display(self):
        print(self.name)


# creating object of the class
obj = myname()

# calling the instance method using the object obj
obj.display()
