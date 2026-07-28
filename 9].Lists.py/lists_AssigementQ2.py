"""
Given a list of numbers, write a python code using loop 
to find and print the largest element
"""
nums = [3, 1, 4, 1, 5, 9, 2, 6]
large = 0
n = len(nums)
for i in range(0,n-1):
     if large <= nums[i]:
         large = nums[i]
print(f"Largest number is {large}")

"""
nums = [-3, -1, -4, -1, -5, -11, -2, -6]
large = float("-inf")
n = len(nums)
for i in range(0,n-1):
     if large <= nums[i]:
         large = nums[i]
print(f"Largest number is {large}")
"""