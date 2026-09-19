marks = {'sci': 56, 'maths': 46, 'eng': 34, 'hist': 67}
print(marks.items())
for sub,mark in marks.items():
    print(f"Subject = {sub}, Marks = {mark}")