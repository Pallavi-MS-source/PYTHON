#Strings are immutable
name="Pallavi Sunagar"
print(name[0])
print(name[-1])

#  string does not supports item assigement 
# name[0]="Z"
# print(name)

#stu is not updated,it has different id 
stu = "Diya"
print(stu,id(stu))
#Override
stu = "Disha"
print(stu,id(stu))