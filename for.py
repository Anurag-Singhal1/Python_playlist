# x =['anurag',25,2.5]
# print(x)
# for i in x:
#     print(i)
# print()      # to print in next line
# y='ANURAG'
# for i in y:
#     print(i)

for i in range(10):   # starting with 0 to 9 , in range stop point is excluded
    print(i,end=" ")
print()
for i in range(11,21,1):   # difference of 1
    print(i,end=" ")
print()
for i in range(20,10,-1):   # descending order
    print(i,end=" ")
print()
for i in range(1,21):
    if i%5!=0 :             # to print elements except 5
        print(i,end=" ")