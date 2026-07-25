""" Write a function power(base,exp)
that returns base raised to exp
using loop-no**operator or pow() allowed
"""

def power(base,exp):
    result = 1
    for i in range(exp):
        result = result * base
    return result
    # result = pow(base, exp)
    # print(result)
    
print(power(5,3))


