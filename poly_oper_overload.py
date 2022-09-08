# polymorphism - one thing has multiple forms
# the 4 ways of implementing polymorphism:   1.DUCK TYPING        2. OPERATOR OVERLOADING     3.METHOD OVERLOADING       4.METHOD OVER-RIDING
# 2+5=7, ----->  2,5,7 r OPERANDS     while      +,= r  OPERATOR

# a =2
# b=3
# c='4'
# d='5'
# print(a+b)                 # here, we simply add the numbers by + operator, internally + also cAlls add method (MAGIC METHOD)
# print(int.__add__(a,b))    # in pgming, we will do everything by help of methods, here add() method to add
# # add() method belongs to int class
# print(c+d)
# print(str.__add__(c,d))
#--------------------------------------------------------------------------------------------------------------
# BEHIND THE SCENES, + calls add()func, - calls sub() func, * calls mul() func, etc...etc....

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        # print("Anurag")

    def __add__(self, other):      # this is operator overloading, we can assign anything to add()func to add, like add 2 objects
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):             # now, this is method over-riding
        return '{} {}'.format(self.m1, self.m2)         #  these curly brackets were replaced by these values

s1 = Student(10,80)
s2 = Student(30,40)
s3  = s1 + s2        # here, we overload the + operator by making add() func to add 2 objects
print(s3.m1,s3.m2)

if s1>s2:            # here, we overload the > operator
    print("s1 Wins")
else:
    print("s2 Wins")

    #  CONCEPT TO LEARN................
a =9
print(a)      # it prints the value of a i.e, 9
print(a.__str__())           # prints 9
# behind the scene, print(a) is  calling the method str()

print(s1)               # but, it prints the address of s1  :  we have to make string by '{} {}'.format()
print(s2)
print(s1.__str__())     #  same prints as print(s1)   : after making str() func it also prints value












