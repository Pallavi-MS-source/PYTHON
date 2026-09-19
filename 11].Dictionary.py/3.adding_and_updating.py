info = { "name":"Pallavi", "age":23}
print(info,id(info))

#Updating(making changes in existing dictionary values)
info["age"] = 20
print(info,id(info))


#Adding(adding new key-value to dictionary)
info["degree"] = "B.E"
print(info,id(info))

# To add multiple key-value
info.update({"gender":"Female", "state":"Karnataka", "ph.no":28734649})
print(info)