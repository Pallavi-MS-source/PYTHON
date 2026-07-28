"""
Create a list containing the squares of numbers from 1 to 10
"""
lst = [1,2,3,4,5,6,7,8,9,10]
def square(lst):
    new_list = []
    for num in lst:
        x = num ** 2
        new_list.append(x)
    return(new_list)
new_list = square(lst)
print(new_list)