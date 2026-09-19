"""
define a dictionary with 5 subjects and their respective marks.Utilize the get()
metod to try accessing a subject that is not in dictionary,ensure it print
"Not Available" by default
"""
# .get() uses key to find value

marks = {'kan': 56,'eng':67,'math':78,'sci':85,'hist':99}
subject = "Biology"
result = marks.get(subject, "Not Available")
print(result)
subject = "kan"
print(marks.get(subject, "Not Available"))
