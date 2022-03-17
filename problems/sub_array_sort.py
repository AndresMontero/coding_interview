def is_out_of_order(i, array):
    if i == 0:
        return array[i] > array[i + 1]
    if i == len(array) - 1:
        return array[i] < array[i - 1]

    return array[i] > array[i + 1] or array[i] < array[i - 1]


def subarraySort(array):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    min_disorder_val = float('inf')
    max_disorder_val = float('-inf')
    min_disorder_idx = 0
    max_disorder_idx = 0

    min_corr_pos = 0
    max_corr_pos = 0

    start_idx = -1
    end_idx = -1

    for i in range(len(array)):
        if is_out_of_order(i, array):
            if array[i] < min_disorder_val:
                min_disorder_idx = i
                min_disorder_val = array[i]
                print(min_disorder_idx, min_disorder_val)
            if array[i] > max_disorder_val:
                max_disorder_idx = i
                max_disorder_val = array[i]
        else:
            continue

    for i in range(len(array)):
        if min_disorder_val < array[i]:
            start_idx = i
            break
    for i in range(len(array) - 1, -1, -1):
        if max_disorder_val > array[i]:
            end_idx = i
            break
    return [start_idx, end_idx]