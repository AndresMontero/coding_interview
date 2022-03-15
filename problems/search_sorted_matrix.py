def searchInSortedMatrix(matrix, target):
    # Write your code here.
    # Time O(n*log(m))
    #
    for row in range(len(matrix)):
        left_pointer = 0
        right_pointer = len(matrix[0]) - 1
        while left_pointer <= right_pointer:

            mid_col = (left_pointer + right_pointer) // 2
            mid_number = matrix[row][mid_col]
            if mid_number == target:
                return [row, mid_col]
            elif mid_number < target:
                left_pointer = mid_col + 1
            else:
                right_pointer = mid_col - 1

    return [-1, -1]


def searchInSortedMatrix_1(matrix, target):
    # Write your code here.
    # Time O(n + m)
    # Space O(1)
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:

        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]

    return [-1, -1]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]
print(searchInSortedMatrix(matrix, 44))
print(searchInSortedMatrix_1(matrix, 44))
