"""
Reverse a list without using.reverse() or list slicing ([::-1])
"""
nums = [1, 2, 3, 5, 7, 9, 11]
n = len(nums)

def rev_list(nums):
    ans = []
    for i in range(n-1,-1,-1):
        x = nums[i]
        ans.append(x)
    return ans

ans = rev_list(nums)
print(ans)