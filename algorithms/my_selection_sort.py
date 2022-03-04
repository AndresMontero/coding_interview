def find_min(arr, pointer):
    tmp_min = arr[pointer]
    min_index = pointer
    for i in range(pointer + 1, len(arr)):

        if arr[i] < tmp_min:
            min_index = i
            tmp_min = arr[i]

    return min_index


def selection_sort(arr):
    size = len(arr)
    for j in range(size - 1):  # iterate over the entire array
        min_index = j
        for i in range(j + 1, size):  # find min index from current position forward
            curr = arr[i]
            if curr < arr[min_index]:
                min_index = i

        if j != min_index:  # Only swap if min index is not already at correct position
            arr[j], arr[min_index] = arr[min_index], arr[j]


if __name__ == '__main__':
    test = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    print(find_min(test, 0))

    test = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    selection_sort(test)
    print(f'sorted array: {test}')

    tests = [
        [21, 38, 29, 17, 4, 25, 11, 32, 9],
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        selection_sort(elements)
        print(f'sorted array: {elements}')
