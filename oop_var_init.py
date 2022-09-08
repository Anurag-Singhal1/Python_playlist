# now, we also declare variable inside this special method(function) called __init__ and it automatically called
# and that's wny we initialise all our variables inside this init func.

# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective: A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that are sent to the function when it is called.

# AN OBJECT HAS ITS OWN METHODS AND VARIABLES and they r working together

class Computer:
    def __init__(self,cpu,ram):         # it  is called automatically, all variables inside this init func
        self.cpu = cpu                  # just initialising/declaring  variables
        self.ram = ram
        # print("in init")

    def config(self):           # we have to call config
        print("Config is ",self.cpu,self.ram)
        # print("i5 , 16GB and 1 TB")

comp1 = Computer('i5',16)               # object bante hi calls init apne aap and init agar mein jo hoga, print kr dega
comp2 = Computer('Ryzen 3',8)               # these comp1 and comp2 r the objects AND SELF is the object which represents all objects
# now every object has its own values.......

comp1.config()
comp2.config()