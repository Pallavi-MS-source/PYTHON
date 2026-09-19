info = {
    'name': 'Pallavi', 
    'age': 20, 
    'degree': 'B.E', 
    'gender': 'Female', 
    'state': 'Karnataka', 
    'ph.no': 28734649
}
print(info,id(info))

info.pop("gender")
print(info,id(info))

# info.clear()          # remove all key-value pair inside dictionary
# print(info,id(info))  # i.e,dictionary becomes empty

# del info             # removes variable(removes from memory)
# print(info)

del info["degree"]      # del can be used anywhere
print(info,id(info))
