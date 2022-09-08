# break a code abcd into a,b,c,d : these r our modules
# module can also be a file, we can also import modules
from mod_calc import *
# import mod_calc                 # then, mod_cal.add/mod_calc.sub          ....etc
# from mod_calc import add

a=9
b=7
c=add(a,b)
d=multi(a,b)
print(c)
print(d)