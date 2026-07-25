count = 0
def increment():
    global count
    count += 1
    print(f"Inside function count = {count}")
increment()
print(f"Outside function count = {count}")
increment()
print(f"Outside function count = {count}")
increment()
print(f"Outside function count = {count}")