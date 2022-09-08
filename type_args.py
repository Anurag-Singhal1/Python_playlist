# def add(x,y):               # here these  X & Y are formal arguments
#     c=x+y
#     print(c)
#
# add(3,6)                    # these are actual arguments

# ACTUAL ARGUMENTS HAS 4 TYPES -    1. position, 2. kewword, 3. default, 4. variable length

# def person(name,age=18):
#     print(name)
#     print(age)
#
# person('anurag',21)                                       # position matters here
# person(name='ANURAG SINGHAL',age=20)                      # keyword
# person('ANURAG',21)                                       # DEFAULT: this 21 comes now and 18 by default if we dont give

# mow, last variable length argument:
def sum(a, *b):
    print(a)
    print(b)
    c=a
    for e in b:
        c=c+e
    print("SUM :",c)

sum(10,12,121, 32.5)                  #  we cant give more than 2 values simply. so ,use *b it can holds all values after a
                               # b forms a tuple of values . and an integer a and tuple cant be add . so, we use for loop

# EXCEPT ALL THESE, THERE IS ALSO ONE : KEYWORD VARIABLE LENGTH ARGUMENTS (KWARGS)