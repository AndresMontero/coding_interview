def maximizeExpression(array):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    if len(array) < 4:
        return 0

    a_values = [array[0]] * len(array)
    a_b_values = [float('-inf')] * len(array)
    a_b_c_values = [float('-inf')] * len(array)
    a_b_c_d_values = [float('-inf')] * len(array)

    for i in range(1, len(array)):
        a_values[i] = max(a_values[i - 1], array[i])

    for i in range(1, len(array)):
        a_b_values[i] = max(a_b_values[i - 1], a_values[i - 1] - array[i])

    for i in range(2, len(array)):
        a_b_c_values[i] = max(a_b_c_values[i - 1], a_b_values[i - 1] + array[i])

    for i in range(3, len(array)):
        a_b_c_d_values[i] = max(a_b_c_d_values[i - 1], a_b_c_values[i - 1] - array[i])

    return a_b_c_d_values[-1]


input = [3, 6, 1, -3, 2, 7]
expected = 4
print(maximizeExpression(input))