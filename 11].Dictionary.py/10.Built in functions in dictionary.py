marks = { 'Bio': 100,'Phy':95,'Chem':99,'Math':96}

# len() number of key-value pair
print(len(marks))

# sum() on values
print(sum(marks.values()))

# min() and max() on values
print(min(marks.values()))
print(max(marks.values()))

# min() and max() on keys (by default it uses keys - sorted alphabetically)
print(min(marks))
print(max(marks))

# sorted() on keys - returns a sorted list of keys
print(sorted(marks))

# sorted dictionary by keys
sorted_by_keys = dict(sorted(marks.items()))
print(sorted_by_keys)k