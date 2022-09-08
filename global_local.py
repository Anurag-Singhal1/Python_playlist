a=10                    # global variable: we can access global variables inside the functions as well if not defined in func
                       # but , we cant access local variable outside that function
print(id(a))

def something():
    # global a                 # to use and update global variable inside the func, but now we cant use local variable
    a=8                      # local variable
    x = globals()['a']
    print(id(x))            # x has same id as a
    globals()['a']=15       # it updates the global variable a from 10 to 15
    print(a)

something()
print(a)

# how can we use same global and local variable in a function: we use globals() func. for this
# globals will give us all the global variables inside that func