def minor(j, matrix):
    reduced_matrix = matrix[1:]
    print(reduced_matrix)
    for i in range(len(reduced_matrix)):
        reduced_matrix[i].pop(j)
        # det_minor = reduced_matrix[0][0] * reduced_matrix[1][1] - reduced_matrix[0][1] * reduced_matrix[1][0]
    return reduced_matrix

def determinant(matrix):
    D = matrix
    N = len(matrix)
    # 1. ensure matrix is square

    # 2. if n == 1, then establish the first base case
    if N == 1:
        return matrix[0]

    # 3. if n == 2, calculate the determinant of the second base case
    elif N == 2:
        return D[0][0] * D[1][1] - D[0][1] * D[1][0]

    # 4. if n > 2, use recursion to calculate the 2 x 2 determinants (i.e., minors)
    elif N > 2:
        # establish for loop, such that k is the number of columns
        # set up an N-1 x N-1 matrix, such that the first row and kth column are removed
        # N-1 rows


        # build the minor from the reduced_matrix
        # k: number of columns

        # loop through each element of the first row (i.e., the cofactors)
        for j in range(len(matrix)):
            matrix1 = minor(j, matrix)
            print(matrix1)





if __name__ == "__main__":
    print(determinant([1]))
    print(determinant([[1, 1], [1, 1]]))
    print(determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))