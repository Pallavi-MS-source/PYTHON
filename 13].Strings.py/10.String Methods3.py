""" SEARCHING and REPLACING
count():Substring frequency
find(): Locate first occurence (returns index)
index():Locate(with error)
replace():Substitute substring"""

text="Pallavi is a coader"
print(text.count(" "))
print(text.find("e"))
print(text.find("x")) #find() returns -1 insted of error 
print(text.index("a"))#index() returns error
print(text.replace("l","b"))
