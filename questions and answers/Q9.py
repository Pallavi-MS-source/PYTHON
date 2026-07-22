"""
Take a student's marks as input. Print their grades
90 and above A
75 to 89 B
60 to 74 C
40 to 59 D
below 40 "Fail"
"""
marks = int(input("Enter marks = "))
if marks >= 90:
    print("A")
elif 75 <= marks <= 89:
    print("B")
elif 60 <= marks <= 74:
    print("C")
elif 40 <= marks <= 59:
    print("D")
else:
    print("Fail")