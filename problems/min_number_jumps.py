def minNumberOfJumps(array):
    # Write your code here.
    # Time O(n^2)
    # Space O(n)
    min_jumps = [float('inf')] * len(array)
    min_jumps[0] = 0

    for i in range(1, len(array)):
        for j in range(i):
            if array[j] + j >= i:
                min_jumps[i] = min(min_jumps[i], min_jumps[j] + 1)

    print(min_jumps)
    return min_jumps[-1]


def minNumberOfJumps_1(array):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    if len(array) <= 1:
        return 0

    max_reach = array[0]
    steps = array[0]
    jumps = 0

    for i in range(1, len(array) - 1):
        max_reach = max(max_reach, array[i] + i)
        steps -= 1

        if steps == 0:
            jumps += 1
            steps = max_reach - i

    print(jumps + 1)

    return jumps + 1


def minNumberOfJumps_2(array):
    # Write your code here.
    # Time O(n^2) worst case | average
    # Space O(1)
    if len(array) <= 1:
        return 0

    jumps = 0
    left = 0
    right = 0

    while right < len(array) - 1:
        farthest = 0
        for i in range(left, right + 1):
            farthest = max(farthest, i + array[i])

        left = right + 1
        right = farthest
        jumps += 1

    print(jumps)
    return jumps


print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
print(minNumberOfJumps_1([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
print(minNumberOfJumps_2([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
