# IN OBJECT, variable to store data and methods for the behaviour
# 2 types:           1. INSTANCE VARIABLE ()                   2. Class(Static) Variable
# if we defined a variable outside __init__ and inside our class : it is class variable
# NAMESPACE - is an area where u create and store object/variable : 1. class namespace    2. object/instance namespace

class Car:
    wheels  =4               # it is a class variable   : it is class namespace where we defined class variables
    def __init__(self):
        self.milage = 10     # these 2 variables r called as instance variables bcz as the object changes, these value also changes
        self.com = "BMW"     # these r just BY DEFAULT value, we can change these

c1 = Car()
c2 = Car()

c1.milage = 21        # this is instance variable
Car.wheels = 5         #  this is how we can also change class variable.....

print(c1.milage,c1.com,c1.wheels)
print(c2.milage,c2.com,c2.wheels)
