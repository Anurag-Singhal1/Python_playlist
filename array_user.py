 # i - iterator
 # e -element

from array import *
arr = array('i',[])
n = int(input("Enter your size of array : "))
for i in range(n):
    x = int(input("Enter your next value "))
    arr.append(x)
print(arr)

val = int(input("Enter value to search : "))
k=0
for e in arr:     # e is element here in arr, we can also took i, e for just convention
    if val==e:
        print(k)
        break
    k+=1
else:
    print("Not found")
print(arr.index(val))  # it is a direct inbuilt function to find index

