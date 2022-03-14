def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def helper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(i, j, array)
            helper(i + 1, array, permutations)
            swap(i, j, array)


def getPermutations(array):
    # Write your code here.
    # Time O(n!)
    # Space O(n*n!)
    permutations = []
    helper(0, array, permutations)

    return permutations


if __name__ == "__main__":
    print(getPermutations([1, 2, 3, 4]))
