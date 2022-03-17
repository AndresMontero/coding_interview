def fourNumberSum(array, targetSum):
    # Write your code here.
    # Time O(n^3)
    # Space O(n)
    array.sort()
    quadruplets = []
    for i in range(len(array)):

        num_1 = array[i]

        for j in range(i + 1, len(array)):
            num_2 = array[j]

            left = j + 1
            right = len(array) - 1

            while left < right:
                if num_1 + num_2 + array[left] + array[right] == targetSum:
                    quadruplets.append([num_1, num_2, array[left], array[right]])
                    left += 1
                    right -= 1
                elif num_1 + num_2 + array[left] + array[right] < targetSum:
                    left += 1
                else:
                    right -= 1

    return quadruplets


def fourNumberSum_1(array, targetSum):
    # Write your code here.
    # Time O(n^2) in average, worst case is O(n^3)
    # Space O(n^2)
    all_pair_sums = {}
    quadruplets = []

    for i in range(1, len(array) - 1):

        for j in range(i + 1, len(array)):
            pair_sum = array[i] + array[j]
            difference = targetSum - pair_sum

            if difference in all_pair_sums:
                for pair in all_pair_sums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])

        for k in range(0, i):
            pair_sum = array[i] + array[k]
            if pair_sum not in all_pair_sums:
                all_pair_sums[pair_sum] = [[array[k], array[i]]]
            else:
                all_pair_sums[pair_sum].append([array[k], array[i]])

    return quadruplets
