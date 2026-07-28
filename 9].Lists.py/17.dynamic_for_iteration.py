matrix = [
    [1,2,3,4,5],
    [2,4,5,6,7],
    [8,6,4,8,9],
    [2,4,6,8,9],
]
rows = len(matrix)
columns = len(matrix[0])
for i in range(0,rows):
    for j in range(0,columns):
        print(matrix[i][j], end = " ")
    print()