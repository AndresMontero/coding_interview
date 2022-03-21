def largestRange(array):
    # Write your code here.
    # Space O(n)
    # Time O(n)
    if len(array) == 1:
        return [array[0], array[0]]

    numbers_dict = {}
    for n in array:
        if n not in numbers_dict:
            numbers_dict[n] = False

    longest_start = 0
    longest_end = 0

    for num in array:
        if numbers_dict[num] == True:
            continue
        numbers_dict[num] = True
        current_length = 1
        upper = num + 1
        while upper in numbers_dict:
            upper += 1
            current_length += 1

        lower = num - 1
        while lower in numbers_dict:
            lower -= 1
            current_length += 1

        start_range = lower + 1
        end_range = upper - 1
        if end_range - start_range >= longest_end - longest_start:
            longest_end = end_range
            longest_start = start_range

    return [longest_start, longest_end]


def largestRange_1(array):
    # Write your code here.
    # Space O(n)
    # Time O(n)
    if len(array) == 1:
        return [array[0], array[0]]
    numbers_set = set(array)
    longest_start = 0
    longest_end = 0

    for num in numbers_set:
        if num - 1 in numbers_set:
            start_range = num - 1
            upper = num + 1
            while upper in numbers_set:
                upper += 1

            end_range = upper - 1
            if end_range - start_range >= longest_end - longest_start:
                longest_end = end_range
                longest_start = start_range

    return [longest_start, longest_end]


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
print(largestRange_1([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
