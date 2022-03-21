def minRewards(scores):
    # Write your code here.
    # Time O(n^2)
    # Space O(n)
    rewards = [1] * len(scores)
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1

        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1

    return sum(rewards)


print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
