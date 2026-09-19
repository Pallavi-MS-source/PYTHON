"""
Create a dictionary for a student including keys like name,age,city and
marks(as a list of score).Print each piece of info using key
"""

student = {"Name":'Raji',"Age":17,"City":'Mangalore',"Marks":[56,67,78,85,99]}
for key in student:
    print(key,student[key])