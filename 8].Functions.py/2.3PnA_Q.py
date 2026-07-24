def find_max(a,b,c):
    if a > b and a > c:
        print(f"Largest is {a}")
    elif b > a and b > c:
        print(f"Largest is {b}")
    else:
        print(f"Largest is {c}")
find_max(8,10,6)