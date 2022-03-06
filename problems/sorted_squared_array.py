def sortedSquaredArray(array):
    # Write your code here.
    # Space O(1)
    # Time (O(n) + O(nlog(n)) => O(nlog(n))
    for i in range(len(array)):
        tmp = array[i]
        array[i] = tmp ** 2

    array.sort()
    return array


def sortedSquaredArray_2(array):
    # Time O(n)
    # Space O(n)
    left_idx = 0
    right_idx = i = len(array) - 1
    solution = [0]*len(array)
    while i >= 0:
        abs_left = abs(array[left_idx])
        abs_right = abs(array[right_idx])

        if abs_left >= abs_right:
            solution[i] = abs_left ** 2
            i -= 1
            left_idx += 1

        else:
            solution[i] = abs_right ** 2
            i -= 1
            right_idx -= 1

    return solution


if __name__ == '__main__':
    array = [1, 2, 3, 5, 6, 8, 9]

    print(sortedSquaredArray(array))
    array = [1, 2, 3, 5, 6, 8, 9]
    print(sortedSquaredArray_2(array))

    array = [1, 4, 9, 16, 25]

    print(sortedSquaredArray_2(array))
    array = [-3, -2, -1]
    print(sortedSquaredArray_2(array))
