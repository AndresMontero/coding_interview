def minimumWaitingTime(queries):
    # Write your code here.
    # Time O(nlog(n))
    # Space O(1)
    queries.sort()
    waiting_time = 0

    for i in range(len(queries)):
        waiting_time += queries[i] * len(queries[i + 1:])

    return waiting_time


if __name__ == '__main__':

    queries = [3, 2, 1, 2, 6]
    print(minimumWaitingTime(queries))
