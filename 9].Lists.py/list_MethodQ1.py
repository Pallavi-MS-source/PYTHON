"""
Find largest and smallest number in list
"""
nums = [1,11,3,2,5,7,9]
n = len(nums)
new_list = sorted(nums)
print(new_list)
print(f"Largest number is {new_list[n-1]}")
print(f"Smallest number is {new_list[0]}")