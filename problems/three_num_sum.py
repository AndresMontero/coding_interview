def threeNumberSum(array, targetSum):
    # Write your code here.
    # Time O(nlog(n)) + O(n^2) => O(n^2)
    # Space O(n)
    result = []


    array.sort()

    for i in range(len(array)):

        num_1 = array[i]
        left = i + 1
        right = len(array) - 1
        while left < right:
            num_2 = array[left]
            num_3 = array[right]
            if num_1 + num_2 + num_3 == targetSum:
                result.append([num_1, num_2, num_3])
                right -= 1
                left += 1
            elif num_1 + num_2 + num_3 < targetSum:
                left += 1
            else:
                right -= 1

    return result

if __name__ == '__main__':
    nums = [12, 3, 1, 2, -6, 5, -8, 6]
    target = 0
    print(threeNumberSum(nums, target))
