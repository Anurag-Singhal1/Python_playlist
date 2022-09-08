# we know something and we do something : so those are variables and methods
# 3 types of methods-           1. instance method         2. class method            3.       static method
# instance has further 2 types:  Accessor methods   and   Mutator Methods
# Accessor methods: if we just want to fetch the value of instance variable
# mutators : if we want to modify the value
# we can use constructor to pass the value or we can use setters
# if u work with instance variable,use instance method and SELF keyword
#  if u work with class vaariable, use class method and CLS  keyword


# NOW, if we do somnething extra, if we want a method which has nothing to do with instance and class variables, then we use static methods


class Student:
    school= "TELUSKO"
    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2= m2
        self.m3= m3

    def avg(self):             # now, this is our instance method bcz it works with objects
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod                   # it is imp to use class methods
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():     # no self and no cls: bcz this method has nothing to do with instance and class variable
        print("This is info Class....")    # EX, if we want to find the factorial of a number.....

# now, for different variables we have different get and set methods...means 3 get and set methods for m1,m2 and m3
#     def get_m1(self):            # getters func  : only fetch value hence ACCESSORS
#         return self.m1
#     def set_m1(self,value):      # setter func  : can modify hence MUTATORS
#         self.m1 = value

s1 = Student(10,20,30)
s2 = Student(40,50,60)

print(s1.avg())                                 # instance method  : uses object
print(Student.getSchool())                      # class method     : find info abt class
Student.info()                                  # static method    : do anything whatever is extra 

# print(s1.m1,s2.m2)    # 10  50        , accessor
