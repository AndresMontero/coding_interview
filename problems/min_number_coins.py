def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    coins_numbers = [float('inf')] * (n + 1)
    coins_numbers[0] = 0
    for d in denoms:
        for amount in range(n + 1):
            if d <= amount:
                coins_numbers[amount] = min(coins_numbers[amount], 1 + coins_numbers[amount - d])
        print(coins_numbers)
    return coins_numbers[n] if coins_numbers[n] != float('inf') else -1

if __name__ == '__main__':
    denoms = [1, 2, 4]
    target = 6

    minNumberOfCoinsForChange(target, denoms)