"""
Take 2 numbers as input. Print the gerater of 2, If they are eaual print "Both are equal"
"""
num1 = int(input(" Enter number 1 ="))
num2 = int(input(" Enter number 2 ="))
if num1>num2:
    print(f"{num1} is greater")
elif num1 < num2:
    print(f"{num2} is greater")
else:
    print(" Both are equal")