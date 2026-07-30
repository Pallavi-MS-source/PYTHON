"""
Create a tuple of marks of 6 students.Print highest,lowest,average,total
"""
marks = (80,99,100,45,67)
n = len(marks)
print(f"Maximum = {max(marks)}")
print(f"Minimum = {min(marks)}")
print(f"Average = {sum(marks)/n}")
print(f"Total = {sum(marks)}")