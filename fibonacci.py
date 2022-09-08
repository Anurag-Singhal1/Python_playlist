# 0,1,1,2,3,5,8,13,21,34,........

def fib(n):
    a=0
    b=1
    if n<=0:
        print("NAsha krna chor do")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

fib(int(input("Enter your value : ")))
