"""
function name = lambda parameter : what to find
"""


# def square(n):
#     return n ** 2
# print(square(5))

square = lambda n:n**2
print(square(5))

# def is_adult(age):
#     if age >= 18:
#         return True
#     return False
# print(is_adult(77))
# print(is_adult(7))

is_adult = lambda age : True if age >= 18 else False
print(is_adult(77))
print(is_adult(7))
