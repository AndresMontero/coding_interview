def getNthFib(n):
    # Time (O(2^n))
    # Space (O(n))
    # Write your code here.
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)


def getNthFib_2(n, memoize={1: 0, 2: 1}):
    # Write your code here.
    # Time (O(n))
    # Space (O(n))

    if n in memoize:
        return memoize[n]

    else:
        memoize[n] = getNthFib_2(n - 1, memoize) + getNthFib_2(n - 2, memoize)

    return memoize[n]


def getNthFib_3(n):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    a = 0
    b = 1

    counter = 3

    while counter <= n:
        tmp = b
        b = a + b
        a = tmp
        counter += 1

    if n > 1:
        return b
    else:
        return a


if __name__ == '__main__':
    print(getNthFib(21))
    print(getNthFib_2(21))
    print(getNthFib_3(21))
