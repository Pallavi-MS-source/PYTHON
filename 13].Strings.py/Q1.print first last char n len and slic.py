"""Take a name as input from user.Print its first and last character
,and total length of the name."""
def details(name):
    a=name[0]
    b=name[-1]
    x=len(name)
    return(f"{a},{b},{x}")

print(details("Pallavi"))

"""Accept a string as input.Print its reverse using slicing"""
def reversing(stringg):
    return(stringg[::-1])
print(reversing("I am Pallavi"))
