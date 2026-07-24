"""
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
"""
for i in range(1,6):
    for j in range(1,6):
        k = i+j
        if k % 2 == 0:
            print("1", end = " ")
        else:
            print("0", end = " ")
    print()