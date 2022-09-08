# class inherit a class  : SUPER /PARENT CLASS          ------->         SUB/CHILD CLASS
# above , that is called as single level inheritance. now, we have also multilevel inheritance
# a->b->c , we have grandfather -> father -> child  and CHILD can access all the features
# MULTIPLE INHERITANCE : a and b are different class. but, c can access both a and b separately.......
# 1. SINGLE LEVEL INHERITANCE     2. MULTILEVEL INHERITANCE               3. MULTIPLE INHERITANCE

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B:
# class B(A):     # now, B is child/sub class of A : this is called inheritance, ab B mein A ke bhi sb features haii
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):               # MULTIPLE INHERITANCE
# class C(B):               # MULTI-LEVEL INHERITANCE
    def feature5(self):
        print("Feature 5 working")

a1=A()
a1.feature1()
a1.feature2()
print()

b1 = B()
b1.feature3()
b1.feature4()
# b1.feature2()
print()

c1 = C()
c1.feature1()
c1.feature5()