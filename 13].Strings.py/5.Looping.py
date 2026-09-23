lang = "python Python"
#for loop
for char in lang:
    print(char)
#while loop
i=0
while i<len(lang):
    print(lang[i])
    i+=1
#enumerate(when we need both index and character)
for index,char in enumerate(lang,start=1):
    print(f"{index} - {char}")
    