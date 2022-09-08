
def count(lst):
    # lst=[1,2,3]
    even=0
    odd=0
    for e in lst:
        if e%2==0:
            even+=1
        else:
            odd+=1
    return even, odd

lst=[1,2,3,4,5,6,7,8,9,13,14,36,68]
 
# even, odd = count([1,2,3,4,5,6,7,8,13,14,36,68])        # passing a list to the function
even, odd = count(lst)

print("EVEN : {} AND ODD : {}".format(even,odd))
print()
print("EVEN : ",even)
print("ODD : ",odd)
