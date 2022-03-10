def maxSubsetSumNoAdjacent(array):
    # Time O(n)
    # Space O(n)
    # Write your code here.
    if len(array) < 1:
        return 0
    if len(array) < 2:
        return array[0]

    max_sums = [0] * len(array)
    max_sums[0] = array[0]
    max_sums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])

    return max_sums[-1]


def maxSubsetSumNoAdjacent_2(array):
    # Time O(n)
    # Space O(1)
    # Write your code here.
    if len(array) < 1:
        return 0
    if len(array) < 2:
        return array[0]

    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current

    return first

if __name__ == '__main__':
    nums = [75, 105, 120, 75, 90, 135]
    print(maxSubsetSumNoAdjacent((nums)))
    print(maxSubsetSumNoAdjacent_2((nums)))
