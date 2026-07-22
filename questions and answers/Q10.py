"""
Take a number as input . Check if it is a leap year ( A year is leap year 
if it is divisible by 4, but not by 100, unless it is also divisible by 400)
"""
# num = int(input(" Enter a year = "))
# if num % 4 == 0 and num % 100 != 0:
#     print(" Leap year")
# elif num % 4 == 0 and num % 100 == 0 and num % 400 == 0
#     print("leap year")
# else:
#     print(" Not leap year")

num = int(input("Enter a year = "))

if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")