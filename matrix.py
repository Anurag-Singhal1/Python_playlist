from numpy import *
# arr = array([
#     [1,2,3,6,2,9],
#     [4,5,6,4,9,0]
# ])
# print(arr)
# print(arr.dtype)
# print(arr.ndim)
# print(arr.shape)       # gives no of rows and columns
# print(arr.size)        # no of elements
#
# arr2 = arr.flatten()    # to print in 1-d from 2-d
# print(arr2)
#
# arr3 = arr2.reshape(3,4)   # to print in multi-dimensional from 1-d
# print(arr3)                # 3 is row, 4 is columns
# print()
# arr4 = arr.reshape(2,2,3)   # 2  2-d arrays, with 2 -rows and 3 columns
# print(arr4)

#-----------------------------------------------------MATRIX------------------------------------------------------------------------------
# arr = array([
#     [1,2,3,4],
#     [5,6,7,8]
# ])
# m = matrix(arr)


# m = matrix('1 2 3; 4 5 6; 7 9 1')   # comma/space anything work here
# print(m)
# print()
# print(diagonal(m))
# print(m.min())
# print(m.max())


m1 = matrix('1 2 3; 4 5 6; 7 9 1')
m2 = matrix('1 5 3; 8 0 6; 9 9 9')
m3 = m1+m2
m4 = m1*m2
print(m3)
print()
print(m4)

