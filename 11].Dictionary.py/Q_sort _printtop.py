"""
Given a dictionary of subjects and their marks,sort it by marks in descending order,
Then print only top 3 subjects with highest marks
"""
subjects={
    "Mathematics":98,
    "Science":99,
    "History":90,
    "English":95,
    "Kannada":97,
    "Hindi":88,
    }
ans=sorted(subjects.items(),key=lambda x:x[1],reverse=True)
print(ans[0:3])
result=ans[0:3]
for details in result:
    print(f"Sub={details[0]},Mark={details[1]}")