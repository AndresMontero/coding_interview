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


def get_local_mins(scores):
    local_mins_idx = []

    if len(scores) == 1:
        return [0]

    for i in range(1, len(scores) - 1):
        if scores[i - 1] > scores[i] and scores[i] < scores[i + 1]:
            local_mins_idx.append(i)

    if scores[0] < scores[1]:
        local_mins_idx.append(0)
    if scores[-1] < scores[-2]:
        local_mins_idx.append(len(scores) - 1)

    return local_mins_idx


def expand_from_local_min_idx(local_min_idx, scores, rewards):
    left_idx = local_min_idx - 1

    while left_idx >= 0 and scores[left_idx] > scores[left_idx + 1]:
        rewards[left_idx] = max(rewards[left_idx], rewards[left_idx + 1] + 1)
        left_idx -= 1

    right_idx = local_min_idx + 1

    while right_idx <= len(scores) - 1 and scores[right_idx] > scores[right_idx - 1]:
        rewards[right_idx] = max(rewards[right_idx], rewards[right_idx - 1] + 1)
        right_idx += 1


def minRewards_1(scores):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    rewards = [1] * len(scores)

    local_mins_idx = get_local_mins(scores)

    for local_min_idx in local_mins_idx:
        expand_from_local_min_idx(local_min_idx, scores, rewards)

    return sum(rewards)


print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
print(minRewards_1([8, 4, 2, 1, 3, 6, 7, 9, 5]))
