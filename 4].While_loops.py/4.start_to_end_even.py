
#start to end print even numbers in series 
start = int(input(" Enter a number to start"))
end = int(input(" Enter a number to stop"))
i = start
while i <= end:
    if i % 2 == 0:
        print(i, end = " ")
    i += 1
