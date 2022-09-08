from numpy import *
# arr = array([1,2,3,4,5])
# arr = arr + 5                                    # to print 5 to all elements
# print(arr)

# arr1 = array([1,2,3,4,5])                           #  to add 2 different arrays
# arr2 = array([3,4,6,82,6])
# arr = arr1 + arr2
# print(arr)
# print(concatenate([arr1, arr2]))

# arr = array([0,1,2,3,4,5,90])
# print(sin(arr))                                       # sin,cos, log, sqrt,min max, sort, unique ---anything
# print(sqrt(arr))
# print("SUM : ",sum(arr))

# ----------------------------------------------------------------------------------------------------------------
               # COPYING AN ARRAY...............
               # two types of copy - shallow copy and deep copy
               # shallow means value dependent on each others   --- view()
               # deep copy, means different from each other     ---copy()
arr1 = array([1,2,3,4,5])
# arr2 = arr1         # simple copying, alicing
arr2 = arr1.view()                      # after using , view() func. we get different address for both the arrays
# arr2 = arr1.copy()
arr1[1] =7
print(arr1)
print(arr2)
print(id(arr1))      # here, we have same id for both the arrays, means both variable pointing to same address
print(id(arr2))