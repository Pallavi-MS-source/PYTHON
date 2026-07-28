marks = [10,20,40,59,60,79,80]

# To get LENGTH
n = len(marks)
print(f"Length of list = {n}")

# MAX
maxi = max(marks)
print(f"Maximum of list = {maxi}")

# MIN
mini = min(marks)
print(f"Minimum of list = {mini}")

# SUM
Total = sum(marks)
print(f"Total of list = {Total}")

# To sort using sorted(), it will always return new list

new_list1 = sorted(marks)   # returns ASCENDING order
print(f"new list = {new_list1}")

new_list2 = sorted(marks,reverse=True)   # returns DESCENDING order
print(f"new list = {new_list2}")