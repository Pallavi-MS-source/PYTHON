lst = ['Pallavi', 624, 'KLE', 347, 2, 'Hubli']
print(lst)

# To add last
lst.append(100)
print(lst)

# To add at index
lst.insert(1,'Sunagar')
print(lst)

# To remove at index
x = lst.pop()
print(x)
print(lst)

y = lst.pop(4)
print(y)
print(lst)

# remove by value
lst.remove('Pallavi')
print(lst)