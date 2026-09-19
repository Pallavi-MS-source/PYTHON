"""
Write a python function named merge_dict(d1,d2) that accepts 2 dictionaries
as argument and returns new dictionary formed by mering them using update()
ensre d1 remains same
"""

def merge_dict(dict1, dict2):
    merge = {}
    merge.update(dict1)
    merge.update(dict2)
    return merge

d1 = {'comb':50, 'powder':40, 'cream':20, 'kajal':30}
d2 = {'Bhagirathi':100, 'Mutturaj':99, 'Pooja':95,
      'Praveen':70, 'Pallavi':60, 'Sahana':35}

print(merge_dict(d1, d2))
print(d1)