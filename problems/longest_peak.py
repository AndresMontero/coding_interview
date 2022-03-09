def longestPeak(array):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    peak_start = 0
    peak_end = 0
    highest = 0

    answer = []

    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            highest = i
            peak_start = i - 1
            peak_end = i + 1
            while peak_start > 0 and array[peak_start] > array[peak_start - 1]:
                peak_start -= 1
            while peak_end < len(array) - 1 and array[peak_end] > array[peak_end + 1]:
                peak_end += 1
        if len(array[peak_start:peak_end + 1]) > len(answer):
            answer = array[peak_start:peak_end + 1]

    if len(answer) < 3:
        return 0
    else:
        return len(answer)


if __name__ == '__main__':
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longestPeak(array))
