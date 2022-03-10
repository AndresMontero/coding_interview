def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    # Time (O(d*n))
    # Space O(n)
    if n == 0:
        return 1

    ways = [0] * (n + 1)

    ways[0] = 1

    for d in denoms:
        for amount in range(1, n + 1):
            if d <= amount:
                ways[amount] += ways[amount - d]

    return ways[n]


if __name__ == '__main__':
    n = 6
    denoms = [1, 5]
    print(numberOfWaysToMakeChange(n, denoms))
