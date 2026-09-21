fruits={"apple","mango","banana","grapes"}
print("pineapple" in fruits)
print("banana" in fruits)

allowed_user=("HOD","Faculty","Staff")
user=input("Enter user: ")
if user in allowed_user:
    print("Access granted")
else:
    print("Access denied")