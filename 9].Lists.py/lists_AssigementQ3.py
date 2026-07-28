"""
Write a program that takes a list and target a number. Use a loop to determine if
the target number exists in the list 
"""

lst = [12,23,34,56,78,90]

def target_number (nums,target):
    for num in lst:
        if num == target:
            return True
    return False
result = target_number(lst,8)   
print(result)
