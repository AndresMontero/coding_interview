def kadanesAlgorithm(array):
    # Write your code here.
    # Time O(n)
    # Space O(n)

    max_start_idx = 0
    max_end_idx = 0
    max_here = array[0]
    max_sum = max_here
    for i in range(1, len(array)):
        if max_here + array[i] > array[i]:
            if max_here + array[i] > max_sum:
                max_end_idx = i
            max_here = max_here + array[i]
        else:
            max_here = array[i]
            max_start_idx = i
        max_sum = max(max_here, max_sum)

    print(max_sum)
    print(sum(array[max_start_idx:max_end_idx + 1]), array[max_start_idx:max_end_idx + 1])
    return max_sum

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(kadanesAlgorithm(nums))
