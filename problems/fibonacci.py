def fibbo_re(n):
    # Base cases
    if n <= 1:
        return n
    # recursive function
    return fibbo_re(n - 1) + fibbo_re(n - 2)


def fibbo_it(n):
    # initial conditions
    a = 0
    b = 1

    for i in range(n):
        tmp = a
        a = b
        b = tmp + b
    return a

if __name__ == '__main__':
    print('Hi')
    for i in range(6):
        print(fibbo_re(i))

    for i in range(6):
        print(fibbo_it(i))
