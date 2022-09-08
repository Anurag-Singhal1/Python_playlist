# poly - many, morph - forms......means an object or 1 thing shows different forms
# we use polymorphism most in LOOSE COUPLING, DEPENDENCY INJECTION, INTERFACE.....

# the 4 ways of implementing polymorphism:   1.DUCK TYPING        2. OPERATOR OVERLOADING     3.METHOD OVERLOADING       4.METHOD OVER-RIDING

# DUCK TYPING: if it looks like a duck, swims like a duck, quacks like a duck, then probably it is a duck.

# x=5                                                 # x is just a name in the memory to the object of type int

# Dynamic typing means that the type of the variable is determined only during runtime. Due to strong typing, types need to be compatible
# with respect to the operand(2+5) when performing operations.

class Pycharm:
    def execute(self):                     # execute function haiii  : duck typing
        print("Compiling")
        print("Running")
class MyEditor:
    def execute(self):                     # execute func haiii  : duck typing
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()                      # execute haiii...

ide = MyEditor()
lap1 = Laptop()
# lap1.code(Pycharm())
# lap1.code(MyEditor())
lap1.code(ide)