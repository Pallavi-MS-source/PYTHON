# Dictionary in dictinary
students = {
    "1":{'Name':'Ravi','Age':20,'City':'Bangalore'},
    "2" : {'Name':'Raju','Age':23,'City':'Belagum'},
    "3":{'Name':'Riya','Age':19,'City':'Bidar'},
    #"3":{'Name':'Riya','Age':19,'City':'Bidar','Details':{'Ph':86180,'Gender':'Female'}},
}
#How to access
print(students["2"])
print(students["2"]["Name"])
#print(students["3"]["Details"]["Ph"])

#Iterating key n values
for roll,details in students.items():
    print(f"k = {roll}, v = {details}")
    print(f"roll = {roll}, details = {details["Name"]}")