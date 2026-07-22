"""
Take a persons age and wheather they have a valid ID (True/False) as input.
Can enter a venue only if they are 18 or older AND have a valid ID . 
Print the appropriate message
"""
age = int(input("Enter person age = "))

valid_id = input("Do you have valid ID ? (True/False):")

if valid_id == "True":
    valid_id = True
else: 
    valid_id = False
    
if age >= 18 and valid_id == True:
    print(" Can enter the venue")
else:
    print(" Cannot enter the venue")
    