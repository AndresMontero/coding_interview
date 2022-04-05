def valid_tree(n: int, edges) -> bool:
    # write your code here

    adj = {i: [] for i in range(n)}

    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visited = set()

    def dfs(node, prev):
        if node in visited:
            return False

        visited.add(node)
        for neigh in adj[node]:
            if neigh == prev:
                continue
            if not dfs(neigh, node):
                return False  # if we found a loop we return false

        return True

    return dfs(0, -1)


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

print(valid_tree(n, edges))
