def merge_two_sorted_lists(a, b):
    final_list = []
    i = 0  # this will be the left index
    j = 0  # this will be the right index
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            final_list.append(a[i])
            i += 1
        else:
            final_list.append(b[j])
            j += 1
    if i < len(a):
        final_list.extend(a[i:])
    if j < len(b):
        final_list.extend(b[j:])

    return final_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [8, 9, 10, 11, 12, 13, 14]

    a = [7]
    b = [2]
    print(merge_two_sorted_lists(a, b))

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        sorted_list = merge_sort(elements)
        print(f'sorted array: {sorted_list}')
