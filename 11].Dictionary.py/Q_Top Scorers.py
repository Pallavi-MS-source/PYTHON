"""
Populate a dictionary with six student names and their corresponding marks.
Loop through it and print the student name who scored above 75
"""
scores = {'Bhagirathi': 100,'Mutturaj': 99,'Pooja':95,'Praveen':70,'Pallavi':60,'Sahana':35}
for name,mark in scores.items():
    if mark > 75:
        print(name)
