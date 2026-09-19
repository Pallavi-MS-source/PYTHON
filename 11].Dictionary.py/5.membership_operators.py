info = {
    'name': 'Pallavi',
    'age': 20, 
    'degree': 'B.E', 
    'state': 'Karnataka', 
    'ph.no': 28734649
} 
# IN (checks only key)
# print("state" in info) 
# print("status" in info)


k = input("Enter key = ")
if k in info:
    print(info[k])
else:
    print("Invalid Key")