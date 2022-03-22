def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def quick_sort_helper(array, start_idx, end_idx):
    if start_idx >= end_idx:
        return

    pivot_idx = start_idx
    left_idx = pivot_idx + 1
    right_idx = end_idx
    while right_idx >= left_idx:
        pivot_number = array[pivot_idx]
        left_number = array[left_idx]
        right_number = array[right_idx]

        if left_number > pivot_number and right_number < pivot_number:
            swap(array, left_idx, right_idx)
        if left_number <= pivot_number:
            left_idx += 1
        if right_number >= pivot_number:
            right_idx -= 1

    swap(array, pivot_idx, right_idx)

    left_sub_array_smaller = right_idx - 1 - start_idx < end_idx - (right_idx + 1)

    if left_sub_array_smaller:
        quick_sort_helper(array, start_idx, right_idx - 1)
        quick_sort_helper(array, right_idx + 1, end_idx)
    else:
        quick_sort_helper(array, right_idx + 1, end_idx)
        quick_sort_helper(array, start_idx, right_idx - 1)


def quickSort(array):
    # Write your code here.
    # Time O(nlog(n)) average | O(n^2) worst case
    # Space O(log(n))
    quick_sort_helper(array, 0, len(array) - 1)

    return array


print(quickSort([8, 5, 2, 9, 5, 6, 3]))
