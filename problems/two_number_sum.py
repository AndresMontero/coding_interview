def twoNumberSum_1(array, targetSum):
    # Space = O(1)
    # Time = O(n^2)

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []



# this other solution uses hash table
def twoNumberSum_2(array, targetSum):
    # Space = O(n) -> hash table
    # Time = O(n) -> traversing array
    numbers_dict = {}
    for n in array:
        tmp = targetSum - n
        if tmp in numbers_dict:
            return [n, tmp]
        else:
            numbers_dict[n] = True

    return []


def twoNumberSum_3(array, targetSum):
    # Space = O(1)
    # Time = O(nlog(n)) from sorting + O(n) from traversing => O(nlog(b)) in total
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        tmp_sum = array[left] + array[right]
        if tmp_sum == targetSum:
            return [array[left], array[right]]

        elif tmp_sum > targetSum:
            right -= 1

        else:
            left += 1

    return []

if __name__ == '__main__':
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10

    print(twoNumberSum_1(array, target))
    print(twoNumberSum_2(array, target))
    print(twoNumberSum_3(array, target))
