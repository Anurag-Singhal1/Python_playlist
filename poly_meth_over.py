#                     METHOD OVERLOADING              &             METHOD OVER-RIDING
# method overloading : if in a class, we have 2 methods with same name but different parameters/arguments
# ex,  average(a,b)            and   average(a,b,c), but in python we dont have this concept, so we cant create 2 methods with same name
# method over-riding: we have 2 methods with same name and same no of parameters but in different class

class Student:
    def __int__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):                # Method Over-Loading......
        s=0
        if a!=None and b!=None and c!=None :
            s = a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a

        return s

s1 = Student()
# print(s1.sum(1,2))
print(s1.sum(3,6))
print()
# ------------------------------------------------METHOD 0VER-RIDING---------------------------------------------------
# until i have not my own phone, my mother's phone is mine and when i get my phone now i print my phone

class A:
    def show(self):
        print("In A Show")
class B(A):
    def show(self):
        print("In B Show")       # my phone over-rides my mother's phone , ab yahi print hoga

a1 = B()
a1.show()








