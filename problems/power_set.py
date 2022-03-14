def powerset(array):
    # Write your code here.
    # Time O(n*2^n)
    # Space O(n*2^n)
    power_sets = [[]]

    for i in range(len(array)):
        for j in range(len(power_sets)):
            current_set = power_sets[j]
            power_sets.append(current_set + [array[i]])

    return power_sets


if __name__ == "__main__":
    print(powerset([1, 2, 3]))
