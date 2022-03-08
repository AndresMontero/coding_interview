def productSum(array, level=1):
    # Write your code here.
    # Time O(n)
    # Space O(depth)
    result = 0
    for i in range(len(array)):
        if type(array[i]) is list:
            result += productSum(array[i], level + 1)
        else:
            result += array[i]
        # print(f"current sum is {level * array[i]}, Current result is {result}")

    return result * level




if __name__ == '__main__':
    print(productSum([1, 2, [3], 4, 5]))
