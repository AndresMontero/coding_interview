def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def build_max_heap(array):
    first_parent_idx = (len(array) - 2) // 2
    for curr_idx in reversed(range(first_parent_idx + 1)):
        sift_down(curr_idx, len(array) - 1, array)


def sift_down(curr_idx, end_idx, heap):
    child_one_idx = curr_idx * 2 + 1

    while child_one_idx <= end_idx:
        child_two_idx = curr_idx * 2 + 2 if curr_idx * 2 + 2 <= end_idx else - 1

        if child_two_idx > -1 and heap[child_two_idx] > heap[child_one_idx]:
            idx_to_swap = child_two_idx
        else:
            idx_to_swap = child_one_idx

        if heap[idx_to_swap] > heap[curr_idx]:
            swap(heap, curr_idx, idx_to_swap)
            curr_idx = idx_to_swap
            child_one_idx = curr_idx * 2 + 1
        else:
            return


def heapSort(array):
    # Write your code here.
    # Time O(nlog(n))
    # Space O(1)
    build_max_heap(array)

    for end_idx in reversed(range(1, len(array))):
        swap(array, 0, end_idx)
        sift_down(0, end_idx - 1, array)

    return array


print(heapSort([8, 5, 2, 9, 5, 6, 3]))
