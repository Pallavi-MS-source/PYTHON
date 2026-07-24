def absolute_value(num):
    if num > 0:
        return f"absolute value is {num}"
    elif num < 0:
        return f"absolute value is {-num} "
    else:
        return f"absolute value is {num}"
print(absolute_value(10))
print(absolute_value(-10))
print(absolute_value(0))
