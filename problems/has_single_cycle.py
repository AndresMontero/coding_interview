def hasSingleCycle(array):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    visited = [0] * len(array)
    visited[0] = 1
    next_to_visit = 0
    for i in range(len(array)):
        next_to_visit += (array[next_to_visit])
        if abs(next_to_visit) > len(array) - 1:
            if next_to_visit > 0:
                next_to_visit = next_to_visit % len(array)
            else:
                next_to_visit = abs(next_to_visit) % len(array)
                next_to_visit *= -1
        visited[next_to_visit] += 1
        print(next_to_visit, visited)

    if visited[0] == 2 and max(visited[1:]) == max(visited[1:]) == 1:
        return True
    return False


def hasSingleCycle_2(array):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    count = 0
    next_to_visit = 0
    for i in range(len(array)):
        next_to_visit += (array[next_to_visit])
        if abs(next_to_visit) > len(array) - 1:
            if next_to_visit > 0:
                next_to_visit = next_to_visit % len(array)
            else:
                next_to_visit = abs(next_to_visit) % len(array)
                next_to_visit *= -1

        count += 1

        if next_to_visit == 0 and count < len(array) - 1:
            return False

    if next_to_visit == 0:
        return True
    return False


if __name__ == "__main__":
    print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
    print(hasSingleCycle_2([2, 3, 1, -4, -4, 2]))
