# replace elements in lower triangular with "*"
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
rows = len(matrix)
columns = len(matrix[0])
for i in range(0,rows):
    for j in range(0,columns):
        if i >= j:
             print(matrix[i][j],end = " ")
        else:
            print("*", end = " ")
    
    print()

# replace elements in upper triangular with "*"
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
rows = len(matrix)
columns = len(matrix[0])
for i in range(0,rows):
    for j in range(0,columns):
        if i <= j:
             print(matrix[i][j],end = " ")
        else:
            print("*", end = " ")
    
    print()