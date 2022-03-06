def isValidSubsequence(array, sequence):
    # Time O(n)
    # Space O(1)
    arr_idx = 0
    seq_idx = 0

    while arr_idx < len(array) and seq_idx < len(sequence):

        if array[arr_idx] == sequence[seq_idx]:
            arr_idx += 1
            seq_idx += 1
        else:
            arr_idx += 1

    return seq_idx == len(sequence)


def isValidSubsequence_2(array, sequence):
    # Time O(n)
    # Space O(1)
    seq_idx = 0

    for n in array:
        if seq_idx == len(sequence):
            break
        if n == sequence[seq_idx]:
            seq_idx += 1
    return seq_idx == len(sequence)


if __name__ == '__main__':
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    target = [1, 6, -1, 10]

    print(isValidSubsequence(array, target))
    print(isValidSubsequence_2(array, target))
