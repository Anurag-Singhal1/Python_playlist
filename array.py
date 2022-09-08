# in this, we too have all the values of same type
# int array, float array  - all the values must be int and float
# array dont have specific size
# i for int, f for flot,d for double, u for unicode(char)

from array import *
vals = array('i',[1,-3,5,7])   # this  i is for int type
# vals.reverse()
print(vals)
print(vals[0])
print(vals.typecode)
print(vals.buffer_info())

# 3 ways to do the same thing
for i in range(4):
    print(vals[i])
for i in range(len(vals)):
    print(vals[i])
for e in vals:
    print(e)

char = array('u',['a','n','u','r','a','g'])
print(char)