def update(x):
    print(id(x))    # here we get same id as 10
    x=8
    print(id(x))    # now, it takes the address of 8
    print(x)

print(id(10))
update(10)   # still prints 8  ,we dont use anything here, pass by value and pass  by reference

