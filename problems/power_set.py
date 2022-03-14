def powerset(array):
    # Write your code here.
    # Time O(n*2^n)
    # Space O(n*2^n)
    power_sets = [[]]

    for element in array:
        for j in range(len(power_sets)):
            current_set = power_sets[j]
            power_sets.append(current_set + [element])

    return power_sets


def powerset_recursive(array, idx=None):
    # Write your code here.
    if len(array) < 1:
        return [[]]

    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]

    element = array[idx]

    subsets = powerset_recursive(array, idx - 1)

    for i in range(len(subsets)):
        current_subset = subsets[i]
        subsets.append(current_subset + [element])

    return subsets


if __name__ == "__main__":
    print(powerset([1, 2, 3]))
    print(powerset_recursive([1, 2, 3],))
