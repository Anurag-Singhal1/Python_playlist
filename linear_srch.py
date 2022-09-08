# code to search an element from list: 2 scenarios,    1. element is in list               2. element is not in list
# in for loop we dont do increment
#First of all = is a assignment operator and == is a comparison operator. = operator is used to assign value to a variable and
# == operator is used to compare two variable or constants

pos =-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:       # we r comparing the value with each value in list
            globals() ['pos'] = i
            return True
        i+=1
    return False

    # for i in range(len(list)):
    #     if list[i]==n:
    #         globals() ['pos']=i
    #         return True
    # return False


list = [5,8,4,6,9,2]
# list[0] = 3
# print(list)
n=4
if search(list,n):
    print("Found at : ",pos+1 )
else:
    print("Not found")
