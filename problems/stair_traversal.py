def staircaseTraversal(height, maxSteps):
    # Write your code here.
    # Sliding window solution
    # Time O(n) where n is the height of the staircase and k is the number of allowed steps
    # Space O(n) height of the recursive calls
    current_number_ways = 0
    ways_to_top = [1]

    for current_height in range(1, height + 1):
        start_prev_window = current_height - maxSteps - 1
        end_window = current_height - 1
        if start_prev_window >= 0:
            current_number_ways -= ways_to_top[start_prev_window]

        current_number_ways += ways_to_top[end_window]
        ways_to_top.append(current_number_ways)

    print(ways_to_top)
    return ways_to_top[-1]


def staircaseTraversal_dp(height, maxSteps):
    # Write your code here.
    # Time O(k*n) where n is the height of the staircase and k is the number of allowed maxSteps
    # Space O(n) height of the recursive calls
    number_steps = [0] * (height + 1)
    number_steps[0] = 1
    number_steps[1] = 1

    for curr_height in range(2, height + 1):
        step = 1
        while step <= maxSteps and step <= curr_height:
            number_steps[curr_height] = number_steps[curr_height] + number_steps[curr_height - step]
            step += 1

    return number_steps[-1]


def aux_stair_case(height, maxSteps, memoize={0: 1, 1: 1}):
    if height in memoize:
        return memoize[height]

    num_ways = 0

    for step in range(1, min(maxSteps, height) + 1):
        num_ways += staircaseTraversal(height - step, maxSteps)

    memoize[height] = num_ways
    return num_ways


def staircaseTraversal_rec(height, maxSteps):
    # Write your code here.
    # Time O(k*n) where n is the height of the staircase and k is the number of allowed steps
    # Space O(n) height of the recursive calls

    return aux_stair_case(height, maxSteps, memoize={0: 1, 1: 1})


if __name__ == "__main__":
    stairs = 40
    maxSteps = 3
    print(staircaseTraversal(stairs, maxSteps))
    print(staircaseTraversal_dp(stairs, maxSteps))
    print(staircaseTraversal_rec(stairs, maxSteps))
