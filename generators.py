# python says us if u want iterators, we will give u generators : generators will give u iterators
# we have to convert a method  into a generator(special function)

# return  will terminate the function but yield will not
#out of 1000 records,if we work only with 1 value at a time, in that case we use Generators, instead of fetching the whole list, we fetch 1-1 value
# we use generators with the help of yield keyword.....

def topten():

    n=1
    while n<=10:
        sq = n*n
        yield sq
        n +=1

    # return 5                  # it simply prints 5
    # yield 5                     # we use yield instead of return here....yield is a special keyword which will make ur function as a GENERATOR
    # yield 6                     # we can write multiple yield statements here
    # yield 7
    # yield 8
    # yield 9

values = topten()
print(values)                 # generator gives u an iterator

# print(values.__next__())          # it gives u 5 here(yield 5) , gives 1 here: n*n
# print(values.__next__())
for i in values:
    print(i)


