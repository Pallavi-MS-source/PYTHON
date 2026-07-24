start = int(input(" Enter a number to start = "))
end = int(input(" Enter a number to stop = "))

# for i in range(start, end+1):
#     print(i) 

total = 0
for i in range(start, end+1):
    total += i

print(total)   