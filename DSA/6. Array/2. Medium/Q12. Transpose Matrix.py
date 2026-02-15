"""Transpose Matrix"""

def transposeMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])

    result = [[0]*row for _ in range(col)]

    for i in range(0,row):
        for j in range(0,col):
            result[j][i] = matrix[i][j]
        
    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transposeMatrix(matrix))