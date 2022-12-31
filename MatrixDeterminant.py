# Collaborators: Peter Domitrovich
def minor(k, matrix):
    temp = []
    for i in range(len(matrix)):
        tempp = []
        for j in range(len(matrix[0])):
            tempp.append(matrix[i][j])
        temp.append(tempp)

    reduced_matrix = temp[1:]

    for i in range(len(reduced_matrix)):
        reduced_matrix[i].pop(k)

    return reduced_matrix

def cofactor(j, matrix):
    return matrix[0][j]*(-1)**(j+1+1)

def determinant(matrix):
    N = len(matrix)
    # 1. ensure matrix is square

    # 2. if n == 1, then establish the first base case
    if N == 1:
        return matrix[0]

    # 3. if n == 2, calculate the determinant of the second base case
    elif N == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # 4. if n > 2, use recursion to calculate the 2 x 2 determinants (i.e., minors)
    elif N > 2:
        # establish for loop, such that k is the number of columns
        # set up an N-1 x N-1 matrix, such that the first row and kth column are removed
        # N-1 rows

        # build the minor from the reduced_matrix
        # k: number of columns

        # loop through each element of the first row (i.e., the cofactors)
        sum = 0
        for j in range(len(matrix)):
            sum += cofactor(j, matrix) * determinant(minor(j, matrix))

        return sum

if __name__ == "__main__":
    print(determinant([1]))
    print(determinant([[4, 6], [3, 8]]))
    print(determinant([[2, 4, 2], [3, 1, 1], [1,2,0]]))
    print(determinant([[1,1,2,3], [4,5,3,2], [5,4,3,3], [3,4,5,6]]))