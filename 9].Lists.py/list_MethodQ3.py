"""
Given 2 lists, merge them into a single new list wihout modifying the original
"""
lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]
 #print(lst1 + lst2)
def merge_list(lst1,lst2):
    n = len(lst1)
    new_list = []

    for i in range(0,n):
    #for num in lst1:
        new_list.append(lst1[i])

    for j in range(0,n):
    #for num in lst2:
        new_list.append(lst2[j])
    return new_list
    
new_list = merge_list(lst1,lst2)
print(new_list)