def shell_sort(arr):
    gap = len(arr) // 2
    i = 0
    while gap > 0:

        for k in range(i, len(arr) - gap, gap):
            for j in range(i, len(arr) - gap - i, gap):
                a = arr[j]
                b = arr[j + gap]
                if a > b:
                    tmp = arr[j]
                    arr[j] = arr[j + gap]
                    arr[j + gap] = tmp

        i += 1

        if i + gap > len(arr):
            gap -= 1
            i = 0

    # when the gap is 1 we do a normal insertion sort
    # for m in range(1, len(arr)):
    #     anchor = arr[m]
    #     for j in range(m-1, -1, -1):
    #         if anchor <= arr[j]:
    #             arr[j + 1] = arr[j]
    #             arr[j] = anchor


if __name__ == '__main__':
    test = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort(test)
    print(f'sorted array: {test}')

    tests = [
        [21, 38, 29, 17, 4, 25, 11, 32, 9],
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        shell_sort(elements)
        print(f'sorted array: {elements}')
