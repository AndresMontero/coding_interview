def nextGreaterElement(array):
    # Write your code here.
    # Time O(n^2)
    # Space O(n)
    to_return = []
    for i in range(len(array)):
        count = 0
        while count <= len(array) - 1:
            next_pos = (i + count) % (len(array))
            if array[next_pos] > array[i]:
                to_return.append(array[next_pos])
                break
            elif array[i] == max(array):
                to_return.append(-1)
                break

            count += 1
    return to_return


def nextGreaterElement_1(array):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    stack = [0]
    result = [-1] * len(array)
    for i in range(2 * len(array)):
        next_pos = i % len(array)
        while len(stack) > 0 and array[next_pos] > array[stack[-1]]:
            result[stack.pop()] = array[next_pos]

        stack.append(next_pos)

    return result


def nextGreaterElement_2(array):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    stack = []
    result = [-1] * len(array)
    for i in range(2 * len(array) - 1, -1, -1):

        next_pos = i % len(array)
        while len(stack) > 0:
            if stack[-1] > array[next_pos]:
                result[next_pos] = stack[-1]
                break
            else:
                stack.pop()

        stack.append(array[next_pos])

    return result


input = [2, 5, -3, -4, 6, 7, 2]
print(nextGreaterElement(input))
print(nextGreaterElement_1(input))
print(nextGreaterElement_2(input))
