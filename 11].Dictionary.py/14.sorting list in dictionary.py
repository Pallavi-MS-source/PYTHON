marks = {
    'Riya':[43,12,98,10,22],
    'Diya':[76,55,34,89,61],
    'Shreya':[20,35,47,68,30],
    'Maya':[35,56,67,29,40],
}
ans = dict(sorted(marks.items(), key = lambda x:x[1][4]))
print(ans)

marks = {
    'Riya':[43,12,98,10,22],
    'Diya':[76,55,34],
    'Shreya':[20,35],
    'Maya':[35,56,67,29,40],
}
ans = dict(sorted(marks.items(), key = lambda x:x[1][-1]))
print(ans)

marks = {
    'Riya':[43,12,98,10,22],
    'Diya':[76,55,34,89,61],
    'Shreya':[20,35,47,68,30],
    'Maya':[35,56,67,29,40],
}
ascending = dict(sorted(marks.items(), key = lambda x:sum(x[1])))
print(ascending)
descending = dict(sorted(marks.items(), key = lambda x:sum(x[1]), reverse = 'True'))
print(descending)