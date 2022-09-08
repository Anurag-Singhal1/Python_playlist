# __init__ is basically a constructor
# u can create object of inner class inside the outer class   OR
# u can create object of inner class outside the outer class provided u use outer class name to call it

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()         # we create object of inner class here itself in __init__(constructor) of outer class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()                 # to print everything in s1.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.ram,self.cpu)

s1 = Student('Anurag', 11)
s2 = Student('Khushi', 21)

s1.show()
# now, can we directly create a object  of inner class  outside : YES.....
# lap1 = Student.Laptop()
# lap1.show()

# lap1 = s1.lap         # 2 different objects
# lap2 = s2.lap


# print(id(lap1))
# print(id(lap2))

# print(s1.lap.brand)
# print(s1.name, s2.name)