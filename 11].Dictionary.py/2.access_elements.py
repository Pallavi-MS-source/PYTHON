# No indexing in dictionary
marks = {'maths': 12, 
'science': 32, 
'english': 40,
}
# print(marks["science"])
# print(marks.get("science"))
# print(marks.get("science",0))
# print(marks.get("biology",0))


subject = "science"
ans = marks.get(subject)
if ans is None:
    print("Subject not found")
else:
    print(f"answer = {ans}")