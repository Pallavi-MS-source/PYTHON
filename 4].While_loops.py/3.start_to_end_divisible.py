# start to end print numbers which are divisible by 3 and 4
start = int(input(" Enter a number to start"))
end = int(input(" Enter a number to stop"))
i = start
while i <= end:
    if i % 3 == 0 and i % 4 ==0:
        print(i)
    i +=1