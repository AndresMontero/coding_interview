def aux_same_bst(array_one, array_two):
    if len(array_one) != len(array_two):
        return False

    if len(array_one) == 0 and len(array_two) == 0:
        return True

    if array_one[0] != array_two[0]:
        return False

    left_one = [x for x in array_one[1:] if x < array_one[0]]
    left_two = [x for x in array_two[1:] if x < array_two[0]]

    right_one = [x for x in array_one[1:] if x >= array_one[0]]
    right_two = [x for x in array_two[1:] if x >= array_two[0]]

    return aux_same_bst(left_one, left_two) and aux_same_bst(right_one, right_two)


def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    # Time (n^2)
    # Space (n^2)
    return aux_same_bst(arrayOne, arrayTwo)


arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
print(sameBsts(arrayOne, arrayTwo))
