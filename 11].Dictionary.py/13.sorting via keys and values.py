marks = {'phy':25,'chem':35,'bio':50,'kan':30,'eng':45}
# ans = sorted(marks.items(), key = lambda x:x[0])
# ans = sorted(marks.items(), key = lambda x:x[1])
ans = dict(sorted(marks.items(), key = lambda x:x[1]))
print(ans)