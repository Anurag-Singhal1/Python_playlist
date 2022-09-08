# abstract classes and abstract methods in python : by default, python dont support these, so we have to do some stuff
# ABC module - abstract base classes  : we can use this to create abstract classes
# we even cant create object of abstract classes

#Abstract base classes cannot be instantiated: instaniated means copying a class with all of its methods and variables

from abc import ABC, abstractmethod
class Computer(ABC):          #  and class which have abstract methods r called AS abstract classes
    @abstractmethod
    def process(self):     # now, this method which only has declaration but dont have any definition r called as ABSTRACT METHODS
        pass
        # print("Anurag Singhal")

class Laptop(Computer):
    # pass
    def process(self):
        print("Anurag Singhal")

# class Whiteboard(Computer):
#     def write(self):                            # ek process() func bhi hona chahiye tha to copy Computer class
#         print("its writing")

class Programmer:
    def work(self,c1):
        print("Solving Bugs")
        c1.process()

# c1 = Computer()
c2 = Laptop()              #  we even cant create this object, so we have to define our method
# c3 = Whiteboard()
p1 = Programmer()

# c1.process()               # now, we got an error , bcz we cant create an object of abstract classes
# c2.process()
p1.work(c2)