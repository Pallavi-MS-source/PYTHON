"""
Write a program that takes a list of numbers, and using a loop,
determines whether it is sorted in ascending order. Print true 
if sorted otherwise false
"""
#nums = [10,20,30,40,50,60,70,80,90]
nums = [90,80,70,60,50,40,30,20,10]
#nums = [60,80,70,60,50,40,30,20,10]

n = len(nums)
def is_sorted(nums):
    for i in range(0,n-1):
        if nums[i] > nums[i+1]:
            return False
    return True
print(is_sorted(nums))