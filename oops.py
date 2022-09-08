# python supports functional programmimg, object oriented programmimg, procedure oriented programmimg......
# function in object oriented programming is called as METHODS.
# objects has 2 things - attributes and behaviour(method)
# i m also an object, my pen, laptop etc everything is laptop
# ex- a phone is designed once and then they r manufactured multiple times, this design in programming we say CLASS
# CLASS - DESIGN\ BLUEPRINT
# OBJECT - INSTANCE(REAL STUFF)

# we define class by class Anurag: and then inside it we have 2 things
#  ATTRIBUTES - VARIABLES
#  BEHAVIOUR - METHODS(fUNCTION)

class Computer:              # class name capital always
    def config(self):        # ye self apne aap aa gya
        print("i5, 16gb and 1 TB ")

comp1 = Computer()
comp2 = Computer()
# now, how to call  a func in class: define class as well as object name
Computer.config(comp1)       # this comp1 is going in self and self is the object which we r passing
Computer.config(comp2)

# we use this syntax more than above
comp1.config()            # this time we use object itself to use the function
comp2.config()


# print(type(comp1))          # computer is our class
# a=8                        # even this a is also an object of int class
# print(a.bit_length())      # a is an object and calling bit_length func here
# print(type(a))              # int,string, float: these r inbuilt class



