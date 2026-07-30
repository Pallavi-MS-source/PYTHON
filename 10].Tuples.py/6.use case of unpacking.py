# Make a list which returns min and max
list1 = [1,2,3,4,5]

def min_max(list1):
    mini = min(list1)
    maxi = max(list1)
    return maxi,mini
    
# print( min_max(list1))
ans1,ans2 = min_max(list1)
print(f"Maximun = {ans1}")
print(f"Minimum = {ans2}")