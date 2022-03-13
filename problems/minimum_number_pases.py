def get_previous_negative_neighbors(x, y, matrix):
    neighbors = []
    if x > 0:
        if matrix[x - 1][y] < 0:
            matrix[x - 1][y] *= -1
            neighbors.append((x - 1, y))

    if x < len(matrix) - 1:
        if matrix[x + 1][y] < 0:
            matrix[x + 1][y] *= -1
            neighbors.append((x + 1, y))

    if y > 0:
        if matrix[x][y - 1] < 0:
            matrix[x][y - 1] *= -1
            neighbors.append((x, y - 1))

    if y < len(matrix[0]) - 1:
        if matrix[x][y + 1] < 0:
            matrix[x][y + 1] *= -1
            neighbors.append((x, y + 1))

    return neighbors


def minimumPassesOfMatrix(matrix):
    # Write your code here.
    # Time O(h*weight)
    # Space O(h*weight)
    next_pass_queue = []
    current_pass_queue = []
    number_pases = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 0:
                next_pass_queue.insert(0, (row, col))

    while len(next_pass_queue) > 0:
        current_pass_queue = next_pass_queue
        next_pass_queue = []

        while len(current_pass_queue) > 0:
            x, y = current_pass_queue.pop()
            previous_negative = get_previous_negative_neighbors(x, y, matrix)
            for neighbor in previous_negative:
                next_pass_queue.insert(0, neighbor)

        number_pases += 1

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] < 0:
                return -1

    return number_pases - 1


if __name__ == "__main__":
    input = [
        [0, -1, -3, 2, 0],
        [1, -2, -5, -1, -3],
        [3, 0, 0, -4, -1],
    ]

    print(minimumPassesOfMatrix(input))
