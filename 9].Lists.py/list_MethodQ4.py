"""
Given a list,remove all duplicate elements while preserving the original order
of the unique items
"""

def find_duplicate(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return(result)

lst = [9,1,2,3,3,4,5,2,6,7,1,9,4]
result = find_duplicate(lst)
print(result)