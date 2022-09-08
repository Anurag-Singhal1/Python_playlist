# it is one of the best way to search, also faster than linear search
# IN binary search, first make sure that values r sorted..........
# L()lower is 1st index, U(upper) is last index  :  now find mid index
# mid index = (Lower + Upper)/2  .............5/2 = 2.5.......i.e,2....int DIVISION
# if search value is smaller then change upper bound & Mid becomes new upper bound
# if search value is bigger then change lower bound & Mid becomes new lower bound

pos =-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid = (l+u)//2             # // bcz we only want integer value

        if list[mid]==n:
            globals()['pos']=mid
            return True            # element milte hi return ho jaana haiiii......
        else:
            if list[mid]<n:
                l=mid+1              # this +1   and   -1  is very imp
            else:
                u=mid-1
    return False

list = [1,4,7,8,12,45,99,102,702,10987,56666]        # list is in ascending order
n=12
if search(list,n):
    print("Found at : ",pos+1)
else:
    print("Not Found")


