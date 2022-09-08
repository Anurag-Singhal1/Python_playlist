def div(a,b):
    # if a<b:
    #     a,b=b,a
    print(a/b)

# div(2,4)    # we also want 2 in this case, i.e, numeraraor always grrater than denominator

# but ,we have to do it without touching the function, kuch alag krna haii
# and here, decorators comes into picture : using decorators we can add the extra features into function

def smart_div(func):  # this func is div function, func as a parameter here
    def inner(a,b):    # function inside a function
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div1= smart_div(div)      # div1 can also be div
div1(3,15)