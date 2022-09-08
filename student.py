# class Student:
#     def __init__(self,s_name,s_regno,s_branch,s_cgpa):
#         self.s_name = s_name
#         self.s_regno = s_regno
#         self.s_branch = s_branch
#         self.s_cgpa = s_cgpa
#
#     def get_branch(self):
#         return self.s_branch
#     def getname(self):
#         return self.s_name
#     def _str_(self):
#         print(f'Hello,{self.s_name},your reg. no. {self.s_regno}')
#
# student1 = Student("Anurag Singhal","20BAI10309","CSE(AI & ML)","9.5")
# print(student1)
#

#---------------------------------------------------------------------------

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):            # self ki jgh abc/kuch bhi likh skte haiii, bs phir abc.name and abc.age bhi krna padega
        print("Hello my name is: " + self.name ," and my age is ", self.age)   # only concatenate str to str, so comma is best instead of +

s1 = Student("Anurag Singhal",21)
s1.myfunc()