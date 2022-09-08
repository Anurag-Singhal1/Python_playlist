# A constructor is a special type of method (function) which is used to initialize the instance members of the class. In C++ or Java,
# the constructor has the same name as its class, but it treats constructor differently in Python. It is used to create an object.

# CONSTRUCTOR IN INHERITANCE,      METHOD RESOLUTION ORDER(MRO)

class A:
    def __init__(self):
        print("in A Init ")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")

class B:
# class B(A):
    def __init__(self):
        # super().__init__()            # we r calling here our super class(A) init
        print("In B Init")   # now, when we call init in B, it will print only this and dont move up

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):                   #  agar  (B,A)  kare, to init B print ho jaayega: left to right
    def __init__(self):
        super().__init__()            # prints only A init , now we have concept of MRO(method resolution order)
                                    # it starts from LEFT to RIGHT, whenever we have multiple inheritance
        print("In C Init")

    def feat(self):
        super().feature2()          # to represent SUPER CLASS we use SUPER METHOD

# a1 = A()
# a1 = B()        # it will still cALL the constructor of A, since we dont have init in B that's why it is going up in A
a1 = C()
a1.feature1()                     # same left to right implies for methods, isliye 1-A wala aa jaayega
a1.feat()
