"""
Given 2 lists of same length, write python code using loop to create a new list
where each element is the sum of corresponding elements from both original list
"""
lst1 = [10,20,30,40,50,60,70,80,90]
lst2 = [90,80,70,60,50,40,30,20,10]
def sum_list(lst1,lst2):
    new_list = []
    n = len(lst2)
    for i in range(0,n):
        total = lst1[i] + lst2[i]
        new_list.append(total)
    return new_list
result = sum_list(lst1,lst2)
print(result)

