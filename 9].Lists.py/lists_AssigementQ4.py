"""
Given a list of numbers, use a loop to calculate and print their average.
You can use len() to get count of elements, but avoid using sum() for the total.
"""
lst = [12,23,34,56,78,90]

n = len(lst)
def average (lst):
    total = 0
    for num in lst:
        total += num
    return total/n
       
#print(average(lst))
result = average (lst)
print(f"Result = {result:.2f}")
