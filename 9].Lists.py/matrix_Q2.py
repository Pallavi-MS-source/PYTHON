# print only diagonal elements otherwise print *
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for i in range(0,3):
    for j in range(0,3):
        if i == j:
            print(matrix[i][j],end = " ")
        else:
            print("*", end = " ")
    print()

# print only anti diagonal elements otherwise print *
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for i in range(0,3):
    for j in range(0,3):
        if i + j == 2:
            print(matrix[i][j],end = " ")
        else:
            print("*", end = " ")
    print()
