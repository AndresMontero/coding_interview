def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    # Time O(nlog(n)) + O(mlog(m) + O(n*m)=> O(n*m)
    # Space O(1)
    smallest = 1e7
    answer = []
    arrayOne.sort()
    arrayTwo.sort()

    for n1 in arrayOne:
        for n2 in arrayTwo:
            if n1 > n2:
                if n1 - n2 < smallest:
                    smallest = n1 - n2
                    answer = [n1, n2]
            elif n1 < n2:
                if n2 - n1 < smallest:
                    smallest = n2 - n1
                    answer = [n1, n2]
            else:
                return [n1, n2]
    return answer


def smallestDifference_2(arrayOne, arrayTwo):
    # Write your code here.
    # Time O(nlog(n)) + O(mlog(m))
    # Space O(1)
    smallest = 1e7
    answer = []
    arrayOne.sort()
    arrayTwo.sort()

    pointer_one = 0
    pointer_two = 0
    size_1 = len(arrayOne)
    size_2 = len(arrayTwo)

    while pointer_one < size_1 and pointer_two < size_2:
        num_1 = arrayOne[pointer_one]
        num_2 = arrayTwo[pointer_two]

        if num_1 == num_2:
            return [num_1, num_2]
        elif num_1 > num_2:
            if num_1 - num_2 < smallest:
                smallest = num_1 - num_2
                answer = [num_1, num_2]
            pointer_two += 1
        else:
            if num_2 - num_1 < smallest:
                smallest = num_2 - num_1
                answer = [num_1, num_2]
            pointer_one += 1

    return answer


if __name__ == '__main__':
    nums_1 = [-1, 5, 10, 20, 28, 3]
    nums_2 = [26, 134, 135, 15, 17]
    print(smallestDifference(nums_1, nums_2))
    print(smallestDifference_2(nums_1, nums_2))
