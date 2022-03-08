def insertionSort(array):
    # Write your code here.
    # Time worst O(n^2), average O(n^2), best (O(n))
    # Space = O(1)
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

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
        insertionSort(elements)
        print(f'sorted array: {elements}')
