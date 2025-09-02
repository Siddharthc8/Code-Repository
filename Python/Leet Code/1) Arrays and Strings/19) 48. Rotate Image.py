def rotate(matrix):
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix

# NOTE : matrix reverse(rows) and transpose (OR) transpose and reverse columns (using for loop)


def rotate(matrix: list[list[int]]) -> None:

    row_n = len(matrix)
    col_n = len(matrix[0])
    # matrix.reverse()

    for i in range(row_n):
        for j in range(i+1,col_n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # return matrix

    for mat in matrix:
        for i in range(len(mat)//2):
            mat[i], mat[row_n-1 - i] = mat[row_n-1 - i], mat[i]

    return matrix

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))
