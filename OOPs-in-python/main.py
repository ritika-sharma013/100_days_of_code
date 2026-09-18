# Everything you create in python is an object 
class Dog:

# A special method called __init__() is used to initialize the properties of the object.
#  It is called automatically when a new object is created.
# It runs only once. 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
# self.name & self.breed are properties of the dog object.

# In order to give properties to the dog object, we can define a method

#     def bark(self):
#         print("whoof whoof")

# dog1= Dog("penny", "labrador")
# dog1.bark()
# print(dog1.name)
# print(dog1.breed)

# dog2= Dog("jacky", "Indian breed")
# dog2.bark() 
# print(dog2.name)
# print(dog2.breed)

# Let's take a class car. 
# car has - brand, model, year, color, price 
class Car:
    def __init__(self,brand,model,year,color,price):
        self.brand = brand
        self.model = model
        self.year = year 
        self.color = color 
        self.price = price

    def start_engine(self):
        print(f"Engine of the car of brand {self.brand} and model {self.model} has started running")

car1 = Car("Toyota", "Camry", 2020, "Red", 30000)
car1.start_engine()
print(car1.brand)

car2 = Car("Honda", "Civic", 2021, "Blue", 25000)
car2.start_engine()

# constructor 






