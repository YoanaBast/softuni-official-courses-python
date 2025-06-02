class MatrixContentError(Exception):
    pass
class MatrixSizeError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length): matrix[i].reverse()

mtrx = []

while True:
    line = input().split()
    if not line:
        if len(mtrx) != len(mtrx[0]):
            raise MatrixSizeError("The size of the matrix is not a perfect square")

        break

    if not all(item.isdigit() for item in line):
        raise MatrixContentError("The matrix must consist of only integers")

    line = list(map(int, line))
    mtrx.append(line)

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')