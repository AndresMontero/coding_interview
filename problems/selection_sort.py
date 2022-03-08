def selectionSort(array):
    # Write your code here.
    # Time worst O(n^2), average O(n^2), Best O(n^2)
    # Space O(1)
    for i in range(len(array)):
        smallest_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest_idx]:
                smallest_idx = j
        if smallest_idx != i:
            array[i], array[smallest_idx] = array[smallest_idx], array[i]

    return array


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        selectionSort(elements)
        print(f'sorted array: {elements}')
