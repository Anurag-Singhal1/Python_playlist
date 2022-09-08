# python dont have multi-dimendional array . so ,we use numpy here i.e, matrix
# numpy have multi-dimensionmal array and as well as 1-d array
# numpy - num means numerical

# here, 6 ways to use an array:-  all functions are coming from numpy itself
#                    1. array()         2. linspace()             3. logspace()
#                    4. arange()         5.zeros()                6. ones()

from numpy import *
# arr = array([1,2,3])   # here, we dont have to specify 'i' for int, it understands automatically
# print(arr)
# print(arr.dtype)

# arr1 = linspace(1,50,50)    # start, stop(included ), the no of parts ,   by default - 50 parts
# print(arr1)

# arr2 = arange(1,15,3)  # same as range, start,stop(excluded), steps
# print(arr2)

# arr3 = logspace(1,40,5)    # start, stop, parts . but, here space is not same b/w elements...acc to log
# print(arr3)
# print('%.2f' %arr3[0])   # 1st element
# print('%.2f' %arr3[4])   # 5th element i.e, last

arr4 = zeros(4)   # By default, all zeros are float....
print(arr4)

arr5  = ones(5,int)
print(arr5)