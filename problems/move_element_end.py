def moveElementToEnd(array, toMove):
    # Write your code here.
    # Time O(n)
    # Space O(1)

    left = 0
    right = len(array) - 1

    while left < right:
        if array[right] == toMove:
            right -= 1

        elif array[left] != toMove:
            left += 1
        else:
            array[right], array[left] = array[left], array[right]
            right -= 1
            left += 1

    return array

if __name__ == '__main__':
    nums_1 = [2, 1, 2, 2, 2, 3, 4, 2]
    target = 2
    print(moveElementToEnd(nums_1, target))
