def removeIslands(matrix):
    # Write your code here.
    islands = []

    visited = [[False for _ in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if visited[row][col]:
                continue

            find_islands(row, col, matrix, visited, islands)

    print(islands)
    for island in islands:
        matrix[island[0]][island[1]] = 0
    return matrix


def find_islands(row, col, matrix, visited, islands):
    ones_to_explore = [[row, col]]
    current_island = []
    while len(ones_to_explore):
        current_one = ones_to_explore.pop()
        i = current_one[0]
        j = current_one[1]

        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_island.append(current_one)

        not_visited_ones = get_unvisited_ones(i, j, matrix, visited)

        for one in not_visited_ones:
            ones_to_explore.append(one)

    to_add = True
    if len(current_island) >= 1:
        for t in current_island:
            if t[0] == 0 or t[1] == 0 or t[0] == len(matrix) - 1 or t[1] == len(matrix[0]) - 1:
                to_add = False
                break
        if to_add:
            for island in current_island:
                islands.append(island)


def get_unvisited_ones(i, j, matrix, visited):
    unvisited_ones = []

    if i > 0 and not visited[i - 1][j]:
        unvisited_ones.append([i - 1, j])


    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_ones.append([i + 1, j])

    if j > 0 and not visited[i][j - 1]:
        unvisited_ones.append([i, j - 1])

    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited_ones.append([i, j + 1])

    return unvisited_ones


if __name__ == "__main__":
    input = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]

    print(removeIslands(input))

