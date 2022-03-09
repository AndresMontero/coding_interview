def mergeOverlappingIntervals(intervals):
    # Write your code here.
    # Time (O(nlog(n)))
    # Space O(n)
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for i in range(1, len(intervals)):
        if result[-1][1] >= intervals[i][0]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])

    return result


if __name__ == '__main__':
    array = [
        [1, 2],
        [3, 5],
        [4, 7],
        [6, 8],
        [9, 10]
    ]
    print(mergeOverlappingIntervals(array))
