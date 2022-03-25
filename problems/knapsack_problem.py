def get_values(matrix, items):
    bag = []
    j = len(matrix[0]) - 1
    curr_row = len(matrix) - 1

    while curr_row > 0:
        if j == 0:
            break

        if matrix[curr_row][j] == matrix[curr_row - 1][j]:
            curr_row -= 1

        else:
            bag.append(curr_row - 1)
            j -= items[curr_row - 1][1]
            curr_row -= 1

    return bag


def knapsackProblem(items, capacity):
    # Write your code here.
    # Time O(n *m), where n is the number of items and m is the max capacity
    # Space O(n*m)

    matrix = [[0 for col in range(capacity + 1)] for row in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        curr_weight = items[i - 1][1]
        curr_value = items[i - 1][0]
        for j in range(capacity + 1):
            if curr_weight > j:
                matrix[i][j] = matrix[i - 1][j]
            else:

                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - curr_weight] + curr_value)

    bag = get_values(matrix, items)
    max_value = matrix[-1][-1]

    print(max_value)
    print(bag)
    return [max_value, bag]


print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))
