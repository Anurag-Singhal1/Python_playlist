# 3 types of errors:  1. Compile Time         2. logical error             3. Run Time Error
# compile error: syntax errors are compile time errors, bcz we get these errors at compile time
# logical error: 2+3 = 4, it is a logical error, here code gets compiled, also gives output but it is not the correct output
# Run time error: code gets compiled,also gives correct output, but 6/0 is infinite, i.e, both the 6 & 0 values r given by user,otheer ex: int ki jagh string kr dena

# Now, compile error is the most easiest error to find out, bcz at the developer side itself u get errors
# logical errors r also easy , they r normally comes in bug as well,  and testing team tests it
# run time error, mistake is done by user, if by mistakely a code file is deleted and other file  is not running now:also run time error
# the moment we get run time error, our execution stops : in banking software, we have to care abt all these things
# so even if u get error, our execution shouldn't be stopped: this is our motto

# for different types of errors, u have to use different types of except block

a= 5
b = 0

try:                                       # it is a critical statement\, here may be we get an error, so just try it...
    print("resource open")
    print(a/b)                             # after getting error, it will jump outside the try statement
    # print("resource closed")
    k = int(input("Enter a number : "))
    print(k)
# except Exception as e:                     # what to do,if we get an error, it will only execute if we get any error in try code
except ZeroDivisionError as e:
    print("Hey, u cant divide a number by zero.......  ", e)     # here, e is error name which is run time error
except ValueError as e:                    # int mein string bhar diya
    print("Invalid Input")                # if valueError occurs, it only prints this invalid input. bcz, we specify it for this error.
except Exception as e:             # here,  exception bcz we dont know the error type
    print(e)                                     # it prints the error
    print("Something Went Wrong.....")
finally:
    print("resource closed")              # it will execute no matter we get an error or not

print("Bye")

# k = int(input("Enter a number : "))                    # it is  Value Error...
#     print(k)