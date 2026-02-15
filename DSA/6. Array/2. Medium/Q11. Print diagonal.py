"""Print diagonal"""

def printDiagonal(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(0,row):
        for j in range(0,col):
            if i == j:
                print(matrix[i][j], end=" ")
            else:
                print("*",end=" ")
        print()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
printDiagonal(matrix)