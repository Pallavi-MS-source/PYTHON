student = { 'Name': 'Rahul','Age': 26,'City':'Delhi'}
# Looping over keys (default behaviour)
for key in student:
    print(key)

# Explicitly looping over keys(same result)
for key in student.keys():
    print(key)

# Looping over values
for value in student.values():
    print(value)

# Looping over key value pair using item()
for key,value in student.items():
    print(f"{key} : {value}")

#Practical use - filter based on values
marks = {'kan': 56,'eng':67,'math':78,'sci':85,'hist':99}
for subject,score in marks.items():
    if score > 90:
        print(f"{subject}: Excellent")
    elif score > 80:
        print(f"{subject}: Good")
    else:
        print(f"{subject}: Need Improvement")

# Counting values that match condition(using .values() directly here)
passed_subject = 0
for score in marks.values():
    if score > 60:
        passed_subject += 1
print(f"Passed Subjects = {passed_subject}")