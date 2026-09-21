# Set Operations: Union(combine sets) and Intersection(finds common elements)
a = {1,2,3,4,2,5}
b = {2,6,7,8,1}
cse = {'abc','nop','efg'}
ece = {'klm','nop','qrs'}
print(a|b) # Union
print(cse.union(ece))
print(cse&ece) # Intersection
print(a.intersection(b))
