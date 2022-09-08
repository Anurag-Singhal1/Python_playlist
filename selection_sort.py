# in bubble sort ,at every iteration we do multiple iteration and do multiple swappping.......
# swapping should be only once and that's why SELECTION SORT COMES INTO picture: we reduce no of swapping here
# in selection sort, we go from start to end and we find either min/max value depend on type of implementation. ex, we go for min value here
# So, in each iteration we just find the min value

def sort(nums):
    for i in range(len(nums)-1):        #  (0-4) total 5 elements, if 6 elements in list, to outer loop mein 1-5 hi aayega, compare ki wajh se inner loop se
        minpos = i                     # idhar humne 1st element ko hi smallest let kr liya
        for j in range(i,len(nums)):                     # 6 exclude rahega range mein : i-5
            if nums[j]<nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        # print(nums)            # prints list after each iteration....

nums= [5,3,8,6,7,2]
sort(nums)
print(nums)


# 2 WAYS TO PRINT ALL ELEMENTS IN A LIST:
# for i in range(len(nums)):
#     print(nums[i])
# print()
# for i in nums:
#     print(i)