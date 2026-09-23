"""Read a sentence from the user.Count and print the total number of vowels
present in it using for loop"""
Sentence=input(f"Enter a sentence : ")
count=0
for ch in Sentence:
    if ch in "aeiouAEIOU":
        count+=1
print(count)