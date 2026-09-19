# dic = { key : value}
#           |        |
#        immutable  mutable
marks = {"maths": 12, "science": 32, "english": 40, "exams": [1,2,3]}
print(marks)
print(type(marks))


# list(mutable) can be given as value but not as key
# tuple(immutable) can be given as key but not as value