# Write a function fizzbuzz(n),that takes a single number
# prints Fizz if divisible by 3
# prints Fizz if divisible by 5
# prints FizzBuzz if divisible by both

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return("Fizz")
    elif n % 5 == 0:
        return("Buzz")
    elif n % 3 == 0 :
        return("FizzBuzz")
    else:
        return(n)
print(fizzbuzz(6))
print(fizzbuzz(15))
print(fizzbuzz(7))
print(fizzbuzz(10))
