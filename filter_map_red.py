from functools import reduce

# FILTER, MAP AND REDUCE..... TEHSE ARE IN-BUILT FUNCTIONS IN PYTHON

# def is_even(n):                  # this is not a reusable func, we need it only once  ....so we use lambda(anonymous func)
#     return n%2==0

nums = [3,2,6,8,4,6,2,9]
# evens = list(filter(is_even, nums))                  # USE TO FILTER THE VALUES FROM A LIST, and also return list :we apply in start
evens = list(filter(lambda n:n%2==0, nums))
print(evens)

#   MAP- NOW, WHEN WE HAVE TO CHANGE EVERY VALUE WE USE MAP, LIKE *2 EACH VALUE, +2 EACH VALUE
#   REDUCE - WHEN WE HAVE TO REDUCE THE VALUES, LIKE MULYIPLY ALL VALUES, ADD ALL VALUES,AVERAGE THE VALUES

# def update(n):
#     return n+2
# doubles = list(map(update,evens))
doubles = list(map(lambda n:n+2,evens))
print(doubles)

# def add_all(a,b):
#     return a+b
# sum = reduce(add_all, evens)
sum = reduce(lambda a,b:a+b , evens) 
print(sum)
