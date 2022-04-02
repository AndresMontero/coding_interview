def create_sequence(max_idx, LIS_idx, array):
    curr_idx = max_idx
    sequence = []
    while curr_idx is not None:
        sequence.append(array[curr_idx])
        curr_idx = LIS_idx[curr_idx]

    return sequence


def longestIncreasingSubsequence(array):
    # Write your code here.
    # Time O(n^2)
    # Space O(n)
    LIS_len = [1] * len(array)
    LIS_idx = [None] * len(array)

    max_len = 1
    max_idx = 0

    for i in range(len(array) - 2, -1, -1):
        curr_num = array[i]
        for j in range(i, len(array)):
            other_num = array[j]
            if other_num > curr_num:
                if 1 + LIS_len[j] > LIS_len[i]:
                    LIS_len[i] = 1 + LIS_len[j]
                    LIS_idx[i] = j
        if LIS_len[i] > max_len:
            max_len = LIS_len[i]
            max_idx = i

    print(max_idx, LIS_idx)
    print(create_sequence(max_idx, LIS_idx, array))
    return create_sequence(max_idx, LIS_idx, array)


print(longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))
