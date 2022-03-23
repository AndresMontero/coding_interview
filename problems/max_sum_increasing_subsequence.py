def maxSumIncreasingSubsequence(array):
    # Write your code here.
    # Time O(n^2)
    # Space O(n)

    max_sums = [num for num in array]
    sequences = [None for x in array]
    max_sum_idx = 0
    max_sum_value = float('-inf')
    for i in range(len(array)):
        curr_num = array[i]

        for j in range(i):
            other_num = array[j]
            if curr_num > other_num and max_sums[j] + curr_num >= max_sums[i]:
                max_sums[i] = max_sums[j] + curr_num
                sequences[i] = j
        if max_sums[i] >= max_sum_value:
            max_sum_value = max_sums[i]
            max_sum_idx = i

    sequence = []
    current_idx = max_sum_idx
    while current_idx is not None:
        sequence.append(array[current_idx])
        current_idx = sequences[current_idx]

    print(max_sums)
    print(max_sum_value)
    print(max_sum_idx)
    print(sequences)
    print(sequence[::-1])
    return [max_sum_value, sequence[::-1]]


print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))
