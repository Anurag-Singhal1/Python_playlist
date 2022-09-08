num =4
for i in range(2,num):  # check from 2 to num-1
    if num%i==0:
        print("Not Prime no")
        break
else:
    print("Prime")