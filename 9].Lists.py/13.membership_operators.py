"""
fruits = ['mango', 'orange', 'banana', 'apple', 'strawberry']
# membership
print('banana' in fruits)
print('dheoij' in fruits)

# non-membership
print('banana' not in fruits)
"""
nums = [3,5,4,56,27,89,10,88,21]
target = int(input("Enter the target = "))
if target in nums:
    nums.remove(target)
    print(nums)
else:
    print("Invalid target")

