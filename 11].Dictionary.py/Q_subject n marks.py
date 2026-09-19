"""
Create a dictionary of 6 subjects and their respective marks.Print the subject
with highest marks and the one with lowest,using max() and min() alongside
lambda function
"""
exam = {'phy': 70, 'chem': 12, 'bio': 34, 'eng': 98,'kan':78, 'hin':67}
maxi= max(exam.items(),key=lambda x:x[1])
print(f"subject with nax mark is{sub}")
mini= min(exam.items(),key=lambda x:x[1])
print(mini)

