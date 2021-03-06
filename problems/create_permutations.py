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


def helper_1(array, perm, permutations):
    if not len(array) and len(perm):
        permutations.append(perm)
    else:
        for i in range(len(array)):
            tmp_array = array[:i] + array[i + 1:]
            new_permutation = perm + [array[i]]
            helper_1(tmp_array, new_permutation, permutations)


def getPermutations_1(array):
    # Write your code here.
    # Time O(n^2*n!) worst case, average O(n*n!)
    # Space O(n*n!)
    permutations = []
    perm = []
    helper_1(array, perm, permutations)
    return permutations


if __name__ == "__main__":
    print(getPermutations_1([1, 2, 3, 4]))
    print(getPermutations([1, 2, 3, 4]))
