def riverSizes_depth(matrix):
    # Write your code here.
    # Time O(w*h)
    # Space O(w*h)
    sizes = []

    visited = [[False for value in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            if visited[row][col]:
                continue
            traverseNode_depth_first(row, col, matrix, visited, sizes)

    return sizes


def riverSizes_breadth(matrix):
    # Write your code here.
    # Write your code here.
    # Time O(w*h)
    # Space O(w*h)
    sizes = []

    visited = [[False for value in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            if visited[row][col]:
                continue
            traverseNode_breadth_first(row, col, matrix, visited, sizes)

    return sizes


def traverseNode_depth_first(i, j, matrix, visited, sizes):
    current_river_size = 0
    nodes_to_explore = [[i, j]]  # this is a stack for a depth first search, if you want breadth you need a queue
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if visited[i][j]:
            continue

        visited[i][j] = True
        if matrix[i][j] == 0:
            continue

        current_river_size += 1
        not_visited_neighbors = get_unvisited_neighbors_depth(i, j, matrix, visited)

        for neighbor in not_visited_neighbors:
            nodes_to_explore.append(neighbor)

    if current_river_size > 0:
        sizes.append(current_river_size)


def traverseNode_breadth_first(i, j, matrix, visited, sizes):
    current_river_size = 0
    nodes_to_explore = [[i, j]]
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if visited[i][j]:
            continue

        visited[i][j] = True
        if matrix[i][j] == 0:
            continue

        current_river_size += 1
        not_visited_neighbors = get_unvisited_neighbors_breadth(i, j, matrix, visited)

        for neighbor in not_visited_neighbors:
            nodes_to_explore.insert(0, neighbor)

    if current_river_size > 0:
        sizes.append(current_river_size)


def get_unvisited_neighbors_depth(i, j, matrix, visited):
    unvisited_neighbors = []

    if i > 0 and not visited[i - 1][j]:
        unvisited_neighbors.append([i - 1, j])

    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_neighbors.append([i + 1, j])

    if j > 0 and not visited[i][j - 1]:
        unvisited_neighbors.append([i, j - 1])

    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited_neighbors.append([i, j + 1])

    return unvisited_neighbors


def get_unvisited_neighbors_breadth(i, j, matrix, visited):
    unvisited_neighbors = []

    if i > 0 and not visited[i - 1][j]:
        unvisited_neighbors.append([i - 1, j])

    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_neighbors.append([i + 1, j])

    if j > 0 and not visited[i][j - 1]:
        unvisited_neighbors.append([i, j - 1])

    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited_neighbors.append([i, j + 1])

    return unvisited_neighbors


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1]
    ]
    print(riverSizes_depth(matrix))
    print(riverSizes_breadth(matrix))
