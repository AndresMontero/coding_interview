def arrayOfProducts(array):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    left_prod = [1] * len(array)
    right_prod = [1] * len(array)
    result = [1] * len(array)
    prod = 1
    for i in range(len(array)):
        left_prod[i] = prod
        prod *= array[i]

    prod = 1
    for j in reversed(range(len(array))):
        right_prod[j] = prod
        prod *= array[j]

    for k in range(len(array)):
        result[k] = left_prod[k] * right_prod[k]
    return result


if __name__ == '__main__':
    matrix = [5, 1, 4, 2]
    print(arrayOfProducts(matrix))
