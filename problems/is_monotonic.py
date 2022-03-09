def isMonotonic(array):
    # Write your code here.
    # Time O(n)
    # Space O(1)

    decreasing = False
    increasing = False

    if len(array) <= 1:
        return True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            decreasing = True
        elif array[i] > array[i - 1]:
            increasing = True
        else:
            pass

        if decreasing == increasing == True:
            return False

    return True


if __name__ == '__main__':
    nums_1 = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    print(isMonotonic(nums_1))
