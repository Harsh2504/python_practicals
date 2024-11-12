#Constructor Destructor
class myself:
    def __init__(self):
        print("Namrata Daphale")
    
    def info(self,age):
        print("Age:",age)
    
    def __del__(self):
        print("Destructor called")

obj = myself()
obj.info(20)
del obj