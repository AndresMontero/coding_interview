def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    # Time O(w*h)
    # Space O(w*h)
    matrix = [[x for x in range(width)] for y in range(height)]

    for i in range(width):
        matrix[0][i] = 1

    for j in range(height):
        matrix[j][0] = 1

    for row in range(1, height):
        for col in range(1, width):
            matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]

    print(matrix)

    return matrix[-1][-1]


if __name__ == "__main__":
    width = 4
    height = 3
    print(numberOfWaysToTraverseGraph(width, height))
