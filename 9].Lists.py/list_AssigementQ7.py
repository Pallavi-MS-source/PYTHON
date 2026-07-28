"""
Given a list of numbers(which may contain duplicates), write a python script that takes 
an integer as input from user and remove all occurence of that integr from list
"""
lst = [1,2,3,1,4,5,1,7,8,9,1]

# def remove_occurence(lst,target):
#     new_list = []
#     for num in lst:
#         if num != target:
#             new_list.append(num)
#     return(new_list)
# print(remove_occurence(lst,1))



def remove_occurence(lst,target):
    while target in lst:
        lst.remove(target) 
        
remove_occurence(lst,1)
print(lst)