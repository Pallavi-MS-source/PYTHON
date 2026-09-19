
"""Take numbers as input from the user one by one.
Skip negative numbers and keep adding the positive ones.
Stop when the user enters 0 and print the total.
(Use both continue and break.)"""

p_sum = 0
while True:
    i = int(input(" Enter numbers = "))
    
    if i == 0:
        break
   
    if i < 0:
        continue

    if i > 0:
        p_sum += i
        

print(p_sum)