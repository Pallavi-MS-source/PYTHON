# i = 0
# while i <= 10:
#     if i % 2 == 0:
#       continue
#     print(i, end = " ")
#     i += 1
"""
When continue is executed, Python skips the remaining statements in the loop
and goes back to the top.
i stays 0 forever, and the loop repeats infinitely.
So i += 1 is never executed.
"""

i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
      continue
    print(i, end = " ")
    