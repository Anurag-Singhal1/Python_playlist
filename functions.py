# 2 steps - defining a function and calling a function
# we define function by def func_name

def greet():                    # these () r compulsary to define a function
    print("HELLO")
    print("GOOD MORNING")
greet()                         # calling a function

# def add(x,y):
#     c=x+y
#     # print(c)                  # to execute the result
#     return c                    # to store the value
#
# result = add(3,7)
# # add(3,8)
# print(result)

def sum_add(x,y):
    # x=3
    # y=2
    c=x+y
    d=x-y
    return c,d
result1, result2 = sum_add(6,8)
print(result1, result2)