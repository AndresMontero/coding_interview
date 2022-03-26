def get_min_spaces(pi, numbers_dict, cache, idx):
    if idx == len(pi):
        return -1

    if idx in cache:
        return cache[idx]

    min_spaces = float("inf")

    for i in range(idx, len(pi)):
        prefix = pi[idx:i + 1]
        if prefix in numbers_dict:
            min_spaces_suffix = get_min_spaces(pi, numbers_dict, cache, i + 1)
            min_spaces = min(min_spaces, min_spaces_suffix + 1)

    cache[idx] = min_spaces

    return cache[idx]


def numbersInPi(pi, numbers):
    # Write your code here.
    # Time O(n^2 for the for loop and the recursive call but because of inmutable idx we add extra n so is n^3)
    # Space O(n + m) where n is the len of pi numbers and m is the numbers in the numbers dict
    numbers_dict = {n: True for n in numbers}
    cache = {}
    min_spaces = get_min_spaces(pi, numbers_dict, cache, 0)

    print(cache)
    return -1 if min_spaces == float("inf") else min_spaces


PI = "3141592653589793238462643383279"
numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
print(numbersInPi(PI, numbers))
