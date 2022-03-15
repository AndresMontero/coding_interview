def threeNumberSort(array, order):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    bucket = {}
    for number in order:
        bucket[number] = 0

    for number in array:
        bucket[number] += 1

    for i in range(len(array)):
        if bucket[order[0]] > 0:
            array[i] = order[0]
            bucket[order[0]] -= 1

        elif bucket[order[1]] > 0:
            array[i] = order[1]
            bucket[order[1]] -= 1

        else:
            array[i] = order[2]
            bucket[order[2]] -= 1

    return array


def threeNumberSort_1(array, order):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    first_value = order[0]
    third_value = order[2]

    first_idx = 0

    for i in range(len(array)):
        if array[i] == first_value:
            array[i], array[first_idx] = array[first_idx], array[i]
            first_idx += 1

    third_idx = len(array) - 1
    for i in range(len(array) - 1, -1, -1):
        if array[i] == third_value:
            array[i], array[third_idx] = array[third_idx], array[i]
            third_idx -= 1

    return array


def threeNumberSort_2(array, order):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    first_idx = 0
    second_idx = 0
    third_idx = len(array) - 1

    while second_idx <= third_idx:
        value = array[second_idx]
        if value == order[0]:
            array[second_idx], array[first_idx] = array[first_idx], array[second_idx]
            first_idx += 1
            second_idx += 1

        elif value == order[1]:
            second_idx += 1

        else:
            array[second_idx], array[third_idx] = array[third_idx], array[second_idx]
            third_idx -= 1
    return array


array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
threeNumberSort(array, order)
print(array)
threeNumberSort_1(array, order)
print(array)
threeNumberSort_2(array, order)
print(array)
