"""
print avg and total marks of student
"""
students ={
    "Poo":[12,14,17],
    "Pravi":[15,16,17],
    "Palla":[12,14,11],
    "Sana":[11,14,17],
    }
for name,marks in students.items():
    total=sum(marks)
    avg=total/len(marks)
    print(f"{name}'s total marks is {total} and average marks is {avg:.2f}")
