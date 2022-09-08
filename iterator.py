nums = [7,8,9,5]

# print(nums[3])

# for i in nums:           # behind the for loop, what works is iterator
#     print(i)

# for i in range(len(nums)):            #  i prints index value here
#     print(i)

it = iter(nums)             # iterator only gives u 1 value at a time
print(it.__next__())        # gives 7 , oth index value
print(it.__next__())        # 8
print(next(it))            # also a way
print()

#--------------TO CREATE UR OWN ITERATOR, WE NEED CLASS AND OBJECT----------------------------------------------

class Topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):                    # we use 2 methods here: iter and next to make our iterator
        return self
    def __next__(self):
        if self.num<=10 :
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration      # to stop NONE after 10 values

values = Topten()
print(next(values))                      # both r same, neeche wala
# print(values.__next__())

for i in values:
    print(i)


