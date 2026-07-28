#1 to 20 only even numbers

new_list = [i for i in range(1,21) if i % 2 == 0]
print(new_list)


new_list = [i for i in range(1,21) if i % 2 == 0 and i % 5 == 0]
print(new_list)

# from 1 to 100 make a list of prime numbers
def is_prime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    return False
prime_list = [i for i in range(1,101) if is_prime(i) == True ]
print(prime_list)



# print maks greater than 45
marks = [23,46,67,54,32,67,89,12,34]
new_list = [num for num in marks if num > 45]
print(new_list)