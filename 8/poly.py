class Cat:
    def sound(self):
        print("Meow") 

class Dog:
    def sound(self):
        print("bark") 


# Function that demonstrates polymorphism
# def animal_sound(animal):
#     print(animal.sound())

# Creating instances of Cat and Dog
cat = Cat()
dog = Dog()
cat.sound()
dog.sound()

# # Passing different objects to the same function
# animal_sound(cat)  # Output: Meow
# animal_sound(dog)