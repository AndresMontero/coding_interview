def findThreeLargestNumbers(array):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    answer = [-1e5] * 3

    for n in array:
        if n >= answer[2]:
            answer[0] = answer[1]
            answer[1] = answer[2]
            answer[2] = n

        elif n >= answer[1]:
            answer[0] = answer[1]
            answer[1] = n
        elif n >= answer[0] and n < answer[1]:
            answer[0] = n

    return answer


if __name__ == '__main__':
    print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))