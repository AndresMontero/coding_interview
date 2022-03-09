def firstDuplicateValue(array):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    elements = {}

    for num in array:
        if num in elements:
            return num
        else:
            elements[num] = 1
    return -1


def firstDuplicateValue_2(array):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    index = 0
    for i in range(len(array)):
        index = abs(array[i]) - 1
        if array[index] < 0:
            return abs(array[i])
        else:
            array[index] = array[index] * -1

    return -1


if __name__ == '__main__':
    array = [2, 1, 5, 2, 3, 3, 4]
    print(firstDuplicateValue(array))
    print(firstDuplicateValue_2(array))
