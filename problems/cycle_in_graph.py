
def node_in_cycle(node, edges, visited, in_stack):

    visited[node] = True
    in_stack[node] = True

    for neighbor in edges[node]:
        if not visited[neighbor]:
            has_cycle = node_in_cycle(neighbor, edges, visited, in_stack)
            if has_cycle:
                return True
        elif in_stack[neighbor]:
            return True

    in_stack[node] = False

    return False

def cycleInGraph(edges):
    # Write your code here.
    # Time O (v*e) where v is vertices or nodes and e is number of edges
    # Space O(v)
    size = len(edges)
    visited = [False for _ in range(size)]
    in_stack = [False for _ in range(size)]

    for node in range(size):
        if visited[node]:
            continue

        has_cycle = node_in_cycle(node, edges, visited, in_stack)

        if has_cycle:
            return True

    return False


if __name__ == "__main__":
    input = [
        [1, 3],
        [2, 3, 4],
        [0],
        [],
        [2, 5],
        []
    ]

    input = [
        [],
        [0, 2],
        [0, 3],
        [0, 4],
        [0, 5],
        [0]
    ]
    print(cycleInGraph(input))
