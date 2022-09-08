# init was a actually a constructor
# every time u created an object , it is allocated to new space. and how much space does it take? size depends on no. of variables we have
# and who is responsible to assign/calculate that memory : here comes CONSTRUCTOR
# we define  SPECIal function __init__ and declares our all variables inside it..........

class Computer:
    def __init__(self):
        self.name = 'Anurag'
        self.age = 20

    def update(self):
        self.age=21

    def compare(self,other):            # who is calling, whom to compare
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()            # this bracket is ur constructor
c2 = Computer()

c2.name = 'Singhal'      # hum aise khud bhi change kr skte hai
# c1.age = 12
c1.update()             # here, self will assigned to c1

if c1.compare(c2):        # self is c1 and other is c2 here
    print("They r same ")
else:
    print("They r different ")

print(c1.name, c1.age)
print(c2.name)

# print(id(c1))                # both, object takes different memory/location in space
# print(id(c2))
