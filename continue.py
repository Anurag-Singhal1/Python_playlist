# for i in range(1,51):
#     if i%3==0 or i%5==0:
#         continue
#     print(i,end=" ")
# print()
# print("Bye")

    # PASS STATEMENT -  we use pass to skip the block, when we dont have to write anythihg inside class or function
for i in range(1,51):
    if i%2!=0:     # to pass all the odd values here
        pass
    else:
        print(i,end=" ")
print("Bye")

def fun():
    pass

a=5

class Human:
    pass
print(a)