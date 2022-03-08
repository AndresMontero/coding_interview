def bubbleSort(array):
    # Write your code here.
    # Time best O(n), average O(n^2), worst O(n^2)
    # Space O(1)
    swapped = False


    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
                swapped = True
        if not swapped:
            break
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
        bubbleSort(elements)
        print(f'sorted array: {elements}')

