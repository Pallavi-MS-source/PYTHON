nums = [10,28,40,18,76,38,99,22]
print(nums, id(nums))
# Sorted (Original list remains same,new list created for sorted list)
new_list = sorted(nums)
print(new_list, id(new_list))

# Sort ( Sorting done in the original list only)
nums.sort()
#nums.sort(reverse=True)
print(nums, id(nums))