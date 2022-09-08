# almost in every sorting tecghnique we use swapping: in swapping we will take a third variable
# after every iteration, biggest element reaches to end of list
# range(len(nums)-1,0,-1)  : here we go from higher index value to lower index value
# range(len(nums))         : here we go from lower index value to higher index value

def sort(nums):
    for i in range(len(nums)-1,0,-1):          # ulta chalega ye, if 6 elements: then 5 to 0, ye last mein -1 ulte order ke liye hi haii  : (0-5),(0-4),(0-3),(0-2),(0-1),(0)
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]= nums[j+1]
                nums[j+1] = temp

nums = [5,3,8,6,7,2]
sort(nums)
print(nums)


# nums.sort()                      # this is in-built sorting function of python
