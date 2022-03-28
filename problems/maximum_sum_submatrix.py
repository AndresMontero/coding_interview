def maximumSumSubmatrix(matrix, size):
    # Write your code here.
    # Time O(n * m * s^2) where n is the number of rows, m is the number of cols and s is the size of
    # Space O(1)
    max_sum = float('-inf')

    for i in range(len(matrix) - size + 1):
        for j in range(len(matrix[0]) - size + 1):
            tmp_sum = 0
            for p in range(i, size + i):
                for q in range(j, size + j):
                    tmp_sum += matrix[p][q]

            max_sum = max(max_sum, tmp_sum)
    return max_sum


def maximumSumSubmatrix_1(matrix, size):
    # Write your code here.
    # Time O(w * h)
    # Space O(w*h)
    max_sum = float('-inf')

    sum_matrix = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]

    sum_matrix[0][0] = matrix[0][0]

    for i in range(1, len(sum_matrix)):
        sum_matrix[i][0] = sum_matrix[i - 1][0] + matrix[i][0]

    for i in range(1, len(sum_matrix[0])):
        sum_matrix[0][i] = sum_matrix[0][i - 1] + matrix[0][i]

    for i in range(1, len(sum_matrix)):
        for j in range(1, len(sum_matrix[0])):
            sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1] + matrix[i][j]

    for i in range(size - 1, len(matrix)):
        for j in range(size - 1, len(matrix[0])):
            tmp_sum = sum_matrix[i][j]

            touches_top = i - size < 0

            if not touches_top:
                tmp_sum -= sum_matrix[i - size][j]

            touches_left = j - size < 0

            if not touches_left:
                tmp_sum -= sum_matrix[i][j - size]

            if not touches_top and not touches_left:
                tmp_sum += sum_matrix[i - size][j - size]

            max_sum = max(max_sum, tmp_sum)

    return max_sum


matrix = [[5, 3, -1, 5], [-7, 3, 7, 4], [12, 8, 0, 0], [1, -8, -8, 2]]
size = 2
print(maximumSumSubmatrix(matrix, size))
print(maximumSumSubmatrix_1(matrix, size))
