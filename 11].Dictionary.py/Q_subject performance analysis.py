"""
Given dictionary of marks of different subjects, loop over its values()
to calculate and print the total marks and the average mark obtained
"""
marks = { 'Bio': 100,'Phy':95,'Chem':99,'Math':96}
total = 0
count = 0
for mark in marks.values():
    total += mark
    count+=1
print(f"Total Marks = {total}")
print(f"Average Marks = {total/count}")
    