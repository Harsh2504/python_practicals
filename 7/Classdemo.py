class demo:
    x = 90
res = demo()
print(res.x)
    
class myself:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def fun1(self):
        print("My name is :",self.name)

ob = myself("Namrata",21)
print(ob.name)
print(ob.age)
ob.fun1()