"""Spliting and Joining
split():Break String into List
join():Combine list into string
"""
text="Pallavi Sunagar is a coder"
print(text.split())
print(len(text.split()))
print(text.split("a"))

my_list=['P','A','L','L','A','V','I']
ans="".join(my_list)
print(ans)
print(type(ans))
my_listt=['P','A','L','L','A','V','I',1,9]
anss="".join(str(ch) for ch in my_listt)
print(anss)
print(type(anss))
