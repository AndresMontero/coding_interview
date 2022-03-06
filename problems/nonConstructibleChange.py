def nonConstructibleChange(coins):
    # Write your code here.
    # Time O(nlog(n)) + O(n) -> O(nlog(n))
    # Space O(1)

    coins.sort()
    min_change = 0
    for c in coins:
        if c > min_change + 1:
            return min_change + 1
        elif c <= min_change + 1:
            min_change += c

    return min_change + 1


if __name__ == '__main__':
    coins = [5, 7, 1, 1, 2, 3, 22]

    print(nonConstructibleChange(coins))
